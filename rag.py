import os
import sys
import warnings
warnings.filterwarnings("ignore")# Suppress warnings for clean terminal output
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq

def main():
    #Set API key and PDF details.
    os.environ["GROQ_API_KEY"] = "YOUR_API_KEY"

    pdf_filename = "sample.pdf"
    persist_directory = "./chroma_db"

    #Verify that the PDF file exists.
    if not os.path.exists(pdf_filename):
        print(f"ERROR: Can't find '{pdf_filename}' in this folder. Please place your PDF here.")
        sys.exit(1)

    #Load the PDF.
    print(f"\n--- [Step 1/4] Loading PDF: {pdf_filename} ---")
    loader = PyPDFLoader(pdf_filename)
    docs = loader.load()
    print(f"Success! Loaded {len(docs)} pages.")

    #Split into Chunks.
    print("\n--- [Step 2/4] Splitting Document into Chunks ---")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(docs)
    print(f"Success! Created {len(chunks)} small text chunks.")

    #Embed text chunks and save to local vector store.
    print("\n--- [Step 3/4] Initializing Local Vector Database ---")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    print("Success! ChromaDB vector database is built.")

    #Connect to Groq LLM.
    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.2)

    

    print("\n=== [Step 4/4] RAG Chatbot is Ready! ===")
    print("Ask a question about your PDF and type 'quit' or 'exit' to end the chat.\n")

    #Main RAG loop
    while True:
        try:
            query = input("\nYour Question: ").strip()
            if not query:
                continue
            if query.lower() in ['exit', 'quit']:
                print("Closing. Goodbye!")
                break

            print("\n[Searching database for matching text...]")
            # Look up the top 3 chunks matching the query.
            relevant_chunks = vectorstore.similarity_search(query, k=3)
            
            print("\n--- SCREENSHOT THIS: RETRIEVED CHUNKS ---")
            context_text = ""
            for idx, doc in enumerate(relevant_chunks):
                print(f"\nChunk {idx+1} (Page {doc.metadata.get('page', 'unknown')}):")
                print(doc.page_content)
                print("-" * 20)
                context_text += doc.page_content + "\n\n"

            # Construct the system prompt manually.
            prompt = f"""You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question.
If you don't know the answer, say that you don't know. Keep it short and factual.

Context:
{context_text}

Question: {query}
Answer:"""

            print("\n[Sending text context to Groq LLM...]")
            #Invoke the LLM
            response = llm.invoke(prompt)
            
            print("\n--- SCREENSHOT THIS: FINAL LLM ANSWER ---")
            print(response.content)
            print("=" * 60)

        except KeyboardInterrupt:
            print("\nClosing. Goodbye!")
            break

if __name__ == "__main__":
    main()