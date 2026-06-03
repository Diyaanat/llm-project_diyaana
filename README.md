# llm-project_diyaana

## Aim:
The goal of this project was to build a functional, multi-turn AI question-answering chatbot system using Python and the Groq API that retains context across a single conversation session.

## Approach Used:
- **Environment Isolation:** Setup a local Python virtual environment (`venv`) to keep project dependencies self-contained.
- **API Integration:** Leveraged the `groq` SDK to connect with the Groq cloud infrastructure.
- **Context Retention:** Implemented a dynamic Python list called `messages` that stores the conversational state (`system`, `user`, and `assistant` roles) and appends history chronologically, passing the full context back to the API on every turn.

## Challenges Faced & Key Observations
- **Model Decommissioning:** The assigned model `llama3-8b-8192` returned an Error 400 because it was deprecated by Groq. I resolved this by upgrading the script to use `llama-3.1-8b-instant`.
- **Parameter Testing:** Experimented with `temperature` adjustments (discovering that `0.0` yields deterministic/repetitive responses while `1.0` sparks high creativity) and `max_tokens` controls response length.
- **Linguistic Capabilities:** Observed that the model handles Spanish effortlessly due to core training data optimization, but struggles with complex Arabic syntax.

## How to Run the Application

### Prerequisites
- Python 3.10 or above installed.
- A valid Groq API Key.

### Setup Instructions
1. Clone this repository or download the source code.
2. Open your terminal and navigate to the project directory:
   ```cmd
   cd llm-project