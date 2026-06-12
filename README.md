# llm-project_diyaana

## Task 1: Simple AI Chatbot.

### Aim:
The goal of this project was to build a functional, multi-turn AI question-answering chatbot system using Python and the Groq API that retains context across a single conversation session.

### Approach Used:
- **Environment Isolation:** Setup a local Python virtual environment (`venv`) to keep project dependencies self-contained.
- **API Integration:** Leveraged the `groq` SDK to connect with the Groq cloud infrastructure.
- **Context Retention:** Implemented a dynamic Python list called `messages` that stores the conversational state (`system`, `user`, and `assistant` roles) and appends history chronologically, passing the full context back to the API on every turn.

### Challenges Faced & Key Observations
- **Model Decommissioning:** The assigned model `llama3-8b-8192` returned an Error 400 because it was deprecated by Groq. I resolved this by upgrading the script to use `llama-3.1-8b-instant`.
- **Parameter Testing:** Experimented with `temperature` adjustments (discovering that `0.0` yields deterministic/repetitive responses while `1.0` sparks high creativity) and `max_tokens` controls response length.
- **Linguistic Capabilities:** Observed that the model handles Spanish effortlessly due to core training data optimization, but struggles with complex Arabic syntax.

### How to Run the Application

#### Prerequisites
- Python 3.10 or above installed.
- A valid Groq API Key.

#### Setup Instructions
Follow these exact steps to set up and run the project locally on your machine:

1. **Clone or Download the Repository:**
   Clone this repository using Git or download the source code zip file and extract it to your computer.

2. **Open Your Terminal:**
   Open your command line interface (Terminal on Mac/Linux or PowerShell / Command Prompt on Windows).

3. **Navigate to the Project Directory:**
   Change your directory to the specific repository folder where the files are stored.

4. **Set Up and Activate a Virtual Environment:**
   Create an isolated environment for this project and activate it by running the commands for your operating system:

   -MAC/Linux
```bash
   python3 -m venv venv
   source venv/bin/activate
```
   -Windows
```bash
   python -m venv venv
   .\venv\Scripts\activate
```
5. **Install Required Packages:**
   Install the necessary Groq dependency using Python's package manager:
```bash
   pip install groq
```
6. **Configure the API Key:**

   -Open the chat.py file in a text editor (like VS Code).

   -Locate the line: api_key="YOUR_API_KEY"

   -Replace "YOUR_API_KEY" with your actual, private Groq API key string and save the file.


7. **Run the Chatbot:**
   Execute the script to start the interactive multi-turn chatbot session:
```bash
   python chat.py
```


## Task 2: Document Retrieval-Augmented Generation (RAG) Chatbot

### Aim:
The goal of this task was to build a local Retrieval-Augmented Generation (RAG) pipeline that allows users to have an interactive conversation with a specific local PDF document (`sample.pdf`) by fetching context dynamically and passing it to an LLM for highly factual answers.

### Approach Used:
- **Document Loading & Extraction:** Utilized `PyPDFLoader` to parse, read, and extract raw text from multi-page PDF documents locally.

- **Text Chunking:** Implemented a `RecursiveCharacterTextSplitter` configured to slice text into 500-character chunks with a 50-character overlap to preserve semantic context across chunk borders.

- **Local Embedding Vectorization:** Employed the HuggingFace `all-MiniLM-L6-v2` transformer model to convert text chunks into dense, multi-dimensional numerical vector embeddings.

- **Vector Database (ChromaDB):** Initialized a local `Chroma` instance to index the vector embeddings and persist them to disk in the `./chroma_db` folder, allowing the database to be queried instantly without re-processing the PDF on every run.

- **Orchestrated Context Retrieval:** Programmed a standard similarity search loop (`vectorstore.similarity_search`) that extracts the top 3 matching text chunks matching the user's input question, wraps them into a system context block, and forwards the curated prompt to the Groq LLM API.

### Challenges Faced & Key Observations
- **Library Architecture Evolution:** The base `langchain` package has decoupled its high-level orchestration modules (like legacy chains). Attempting to use old tutorial syntax caused persistent `ModuleNotFoundError` flags. I resolved this by bypassing complex layout abstractions and utilizing standard Python formatting to feed the retrieved context directly into the model via `.invoke()`.

- **API Model Adjustments:** Similar to Task 1, updated the engine from the decommissioned `llama3-8b-8192` model to `llama-3.1-8b-instant` to prevent bad request status codes.

- **Context Pinpointing:** Observed that semantic similarity matching works cleanly to retrieve specific page citations (e.g., matching a question about insurance types directly to Page 9 chunks) without feeding irrelevant pages into the LLM context window.

### How to Run the Application

#### Additional Prerequisites
- The underlying environment from Task 1 must be active.

- A local target PDF saved explicitly as `sample.pdf` inside your working project folder.

#### Setup Instructions

1. **Verify Your Environment State:**
   Ensure your terminal workspace is pointing inside the project folder and the virtual environment is fully engaged:

   -MAC/Linux:
```bash
   source venv/bin/activate
```
   -Windows:
```bash
   .\venv\Scripts\activate
```

2. **Install Required RAG Packages:**
   Install the vector database, parsing, and embedding utilities directly into your existing setup:
```bash
   pip install langchain-community chromadb sentence-transformers pypdf --only-binary=:all:
```
3. **Configure the API Key:**
   -Open the rag.py file in your preferred code editor.

   -Locate the line inside main() setting the environment variable: os.environ["GROQ_API_KEY"] = "YOUR_API_KEY"

   -Paste your private Groq API key string between the quotes and save.

4. **Execute the RAG Chatbot Loop:**
   Launch the system script to build/load the vector index and begin querying your document:
```bash
   python rag.py
```
   **Sample questions to ask:**

      -What is money back policy?

      -How do you choose the right type of insurance?

      -What are the challenges with cashless facility ?