🏥 Clinical Explainable RAG System

An advanced Retrieval-Augmented Generation (RAG) application built with Streamlit, combining local medical knowledge, real-time web search, and LLM reasoning to provide explainable, traceable, and safer AI-generated clinical answers.

🚀 Features
🧠 Hybrid RAG Architecture
Switches intelligently between local knowledge base and web search


🌐 Real-time Web Retrieval
Uses Tavily API to fetch up-to-date medical information with source URLs
🔍 Explainability Layer

Shows:
Retrieved content
Model input context
Source attribution per sentence

🛡️ Hallucination Detection
Labels each sentence as:
🟢 Grounded
🟡 Weakly Grounded
🔴 Possible Hallucination
📊 Confidence Scoring

Dynamic confidence score based on:
Source (local/web)
Context size

🧾 Traceable AI Output
Full transparency of:
LLM input
Retrieved chunks
Final generated answer

🎨 Modern UI
Styled Streamlit interface with clean clinical dashboard look

🏗️ Tech Stack

Python
Streamlit
LangChain
Hugging Face Embeddings
Chroma Vector Database
Groq LLM (LLaMA 3.1)
Tavily Search API

📦 Installation
Clone the repository:
git clone https://github.com/your-username/clinical-rag-system.git
cd clinical-rag-system

Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Install dependencies:
pip install streamlit langchain langchain-huggingface langchain-chroma tavily-python groq

🔐 Environment Variables (IMPORTANT)

⚠️ Do NOT hardcode API keys in production.

Create a .env file:

GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key

Update your code to load them securely:

import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
▶️ Running the App
streamlit run app.py

Open in browser:

http://localhost:8501

🧠 How It Works
1. Query Routing
The system checks similarity against local medical documents
If relevant → uses local DB
Else → performs web search

2. Retrieval
Local स्रोत (Database)
Uses Chroma vector search
Web Source
Uses Tavily API to fetch top results + URLs

3. Chunking
Text is split using RecursiveCharacterTextSplitter
Ensures optimal context size for LLM

4. LLM Generation
Model: llama-3.1-8b-instant via Groq
Prompt constrained to retrieved context only

5. Explainability & Safety
Each sentence is:
Mapped to a source (URL / local DB)
Checked for grounding against context

6. Confidence Score

Calculated based on:

Source type
Context length

📊 Example Use Cases

Try asking:

What causes fever?
Symptoms of viral infection
What is diabetes?
Asthma treatment options
Latest treatment for lung disease

📁 Project Structure
clinical-rag-system/
│
├── app.py              # Main Streamlit application
├── README.md           # Documentation
└── requirements.txt    # Dependencies (optional)

⚠️ Important Disclaimer

🚨 This application is for educational and demonstration purposes only.
It is NOT a substitute for professional medical advice, diagnosis, or treatment.

Always consult a qualified healthcare provider for medical concerns.

🛠️ Future Improvements
🏥 Integrate real clinical datasets (FHIR / EHR)
🧠 Add medical-specific LLM fine-tuning
📊 Improve hallucination detection with NLP metrics
🔐 Add authentication & audit logging
☁️ Deploy on cloud (AWS / GCP / Azure)
📈 Add feedback loop for continuous learning