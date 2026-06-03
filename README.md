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
   Change your directory to the specific repository folder where the files live by running:
```bash
   cd llm-project_diyaana
```
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
6. Configure the API Key:
   -Open the chat.py file in a text editor (like VS Code).
   -Locate the line: api_key="YOUR_API_KEY"
   -Replace "YOUR_API_KEY" with your actual, private Groq API key string and save the file.

7. Run the Chatbot:
   Execute the script to start the interactive multi-turn chatbot session:
```bash
   python chat.py
```