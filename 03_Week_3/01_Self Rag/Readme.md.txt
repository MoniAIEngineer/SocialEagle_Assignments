🧠 Self-RAG (LLM-Free Retrieval-Augmented Generation)

A lightweight and fully deterministic RAG system built with Streamlit and FAISS, demonstrating how to perform question answering without using any Large Language Model (LLM).

This project highlights a Self-RAG approach, where answers are extracted directly from retrieved context using rule-based logic.

🚀 Features
⚡ LLM-Free Architecture
No external APIs or LLM calls
Fully offline and deterministic

🔍 Semantic Retrieval
Uses Hugging Face embeddings for similarity search

🧠 Rule-Based Answer Extraction
Extracts answers directly from retrieved documents

📚 FAISS Vector Store
Fast and efficient in-memory search

🎯 Zero Hallucination
Answers strictly come from existing knowledge base

🎨 Simple UI
Built with Streamlit for easy interaction

🏗️ Tech Stack
Python
Streamlit
FAISS (Vector Search)
Hugging Face Embeddings
LangChain Community Modules

📦 Installation
Clone the repository:
git clone https://github.com/your-username/self-rag.git
cd self-rag

Create a virtual environment:
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

Install dependencies:
pip install streamlit faiss-cpu sentence-transformers langchain

▶️ Running the App
streamlit run app.py

Open in browser:

http://localhost:8501
🧠 How It Works
1. Knowledge Base
A small set of predefined documents is stored

2. Embeddings

Converts documents into vector representations using:

sentence-transformers/all-MiniLM-L6-v2

3. Retrieval
FAISS retrieves the most relevant documents based on query similarity

4. Extractive Answering (No LLM)
Uses rule-based logic to:
Match query intent
Extract exact answers from context

5. Output

Displays:
Retrieved context

Final extracted answer
📊 Example Queries

Try:

Who founded Tesla?
What is the capital of France?
What is the capital of Germany?
What is Python used for?

📁 Project Structure
self-rag/
│
├── app.py              # Main Streamlit application
├── README.md           # Documentation
└── requirements.txt    # Dependencies (optional)

🎯 Design Principles
✅ No LLM dependency
✅ Deterministic outputs
✅ Zero hallucination
✅ Fast and lightweight
✅ Easy to understand RAG basics

⚠️ Limitations
Limited to predefined rules
Not scalable for complex queries
No natural language generation
Requires manual logic updates

🛠️ Future Improvements
🧠 Add LLM-based generation (Hybrid RAG)
📊 Expand knowledge base
🔍 Improve query understanding
🧠 Replace rules with ML-based extraction
☁️ Deploy as API or web service
🤝 Contributing

Contributions are welcome!

Fork the repository
Create a feature branch
Submit a pull request

📄 License

This project is licensed under the MIT License.

🙌 Acknowledgements
Hugging Face for embeddings
FAISS for vector search
Streamlit for UI framework
LangChain community modules