# Conversational AI ChatBot 🤖

This is a simple conversational AI chatbot built using **LangChain** and **Google Generative AI (Gemini)**.  
It maintains chat history and responds in a human-like conversational manner.

---

## Features ✨
- Uses **Google Gemini (gemini-1.5-flash)** model for responses.
- Maintains **chat history** using `SystemMessage`, `HumanMessage`, and `AIMessage`.
- Simple **interactive CLI chatbot**.
- Supports environment variable management with **dotenv**.

---

## Installation ⚙️

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AbhiRaj2802/Conversational-AI-ChatBot.git
   cd Conversational-AI-ChatBot
2. Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
Install dependencies:

3. pip install -r requirements.txt

4. Set up API Key

Create a .env file in the project directory.

Add your Google API key:

GOOGLE_API_KEY=your_api_key_here

5. Run the chatbot:

python chatbot.py

6. Example conversation:

You: Hello
Mr.Fixit: Hi there! How can I assist you today?

You: Tell me a joke
Mr.Fixit: Why don’t skeletons fight each other? Because they don’t have the guts!

7. File Structure 📂
Conversational-AI-ChatBot/
│── chatbot.py        # Main chatbot script
│── requirements.txt  # Required dependencies
│── .env              # API key (not to be committed)
│── README.md         # Project documentation

8. requirements.txt

langchain
langchain-google-genai
python-dotenv
