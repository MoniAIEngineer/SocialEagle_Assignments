🏥 AI Healthcare Assistant (RAG with Groq + Chroma)

An intelligent AI-powered healthcare assistant built using Streamlit, LangChain, Chroma vector database, and Groq LLM (LLaMA 3.1).

This project demonstrates a Retrieval-Augmented Generation (RAG) approach to provide safe, context-based medical information while minimizing hallucinations.

🚀 Features

🧠 RAG-Based Healthcare Assistant
Retrieves relevant medical information before generating answers

🔍 Semantic Search
Uses Hugging Face embeddings for accurate similarity matching

⚡ Fast LLM Inference
Powered by Groq (LLaMA 3.1)

📚 Predefined Medical Knowledge Base
Covers common conditions like:
Fever
Diabetes
Asthma
Migraine
Hypertension

🛡️ Safe AI Design
Strict prompt rules:
No diagnosis
No medication suggestions
Only context-based answers

🧹 Duplicate Removal
Ensures clean and unique search results

🎨 Simple UI
Built with Streamlit for easy interaction

🏗️ Tech Stack
Python
Streamlit
LangChain
Hugging Face Embeddings
Chroma Vector Store
Groq API (LLaMA 3.1)

📦 Installation

Clone the repository:
git clone https://github.com/your-username/ai-healthcare-assistant.git
cd ai-healthcare-assistant

Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

Install dependencies:
pip install streamlit langchain langchain-huggingface langchain-chroma groq
🔐 Environment Setup

⚠️ Do NOT hardcode API keys in production

Create a .env file:

GROQ_API_KEY=your_groq_api_key

Update your code:

import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
▶️ Running the App
streamlit run app.py

Open in browser:

http://localhost:8501
🧠 How It Works
1. Knowledge Base
A predefined set of healthcare-related information is stored

2. Embeddings

Converts text into vectors using:

sentence-transformers/all-MiniLM-L6-v2

3. Vector Search
Uses Chroma to retrieve top relevant documents

4. Context Creation
Top results are combined into a context block

5. LLM Generation
Groq (LLaMA 3.1) generates answers using:
Only retrieved context
Safety constraints

6. Output
Displays:
Relevant medical info
AI-generated explanation
Safety disclaimer

📊 Example Queries

Try:

What causes fever?
Symptoms of diabetes
What is asthma?
Why do we get headaches?
What is dehydration?

📁 Project Structure
ai-healthcare-assistant/
│
├── app.py              # Main Streamlit app
├── README.md           # Documentation
└── requirements.txt    # Dependencies (optional)
