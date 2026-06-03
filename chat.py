import os
from groq import Groq

# Initialize Groq client using the API key.
client = Groq(api_key="YOUR_API_KEY")

# Initialize chat history with system instructions.
messages = [
    {
        "role": "system",
        "content": "You are a calm and helpful assistant named bubbles. Keep your answers upbeat but not over the top. Use emojis and internet and genZ slang but make it feel authentic and dont overdo it. Intorduce yourself as bubbles and ask how you can help."
    }
]

print(" AI Chatbot is ready! Type 'quit' to exit.\n")

# Main conversation loop.
while True:
    user_input = input("You: ")
    
    # Exist conditions.
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
        
    # Skip empty inputs.
    if not user_input.strip():
        continue

    # Save user message to history.
    messages.append({"role": "user", "content": user_input})

    try:
        # Call Groq API with full conversation history.
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.6,      
            max_tokens=200,        
        )

        # Extract and print response
        ai_response = completion.choices[0].message.content
        print(f"AI: {ai_response}\n")

        # Save AI response to history
        messages.append({"role": "assistant", "content": ai_response})

    except Exception as e:
        print(f"An error occurred: {e}")