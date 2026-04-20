🚀 CRAG PRO++ (Explainable Corrective RAG)

An advanced Corrective Retrieval-Augmented Generation (CRAG) system built with Streamlit, featuring retrieval, reranking, filtering, corrective loops, and full explainability trace.

This project demonstrates how to build a robust, transparent, and self-correcting RAG pipeline using open-source models like FLAN-T5 and FAISS vector search.

🌟 Key Highlights
🔁 Corrective RAG Pipeline
Automatically retries retrieval when relevance is low

🧠 Explainability Layer (Trace)

Step-by-step execution logs:
Retrieval
Reranking
Filtering
Correction

📊 Semantic Reranking
Uses cosine similarity for better document ranking

🧹 Dynamic Filtering
Removes low-relevance documents using thresholds

📈 Confidence Scoring
Based on semantic similarity between query and context

🤖 LLM Integration
Uses FLAN-T5 (google/flan-t5-base) for answer generation

⚡ Fast Vector Search
Powered by FAISS

🏗️ Tech Stack
Python
Streamlit
Hugging Face Transformers (FLAN-T5)
Sentence Transformers
FAISS Vector Store
LangChain (Community modules)

📦 Installation
Clone the repository:
git clone https://github.com/your-username/crag-pro-plus.git
cd crag-pro-plus

Create a virtual environment:
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

Install dependencies:
pip install streamlit transformers sentence-transformers faiss-cpu langchain
▶️ Running the App
streamlit run app.py

Open in browser:

http://localhost:8501

🧠 How It Works
1. Retrieval
Fetches top documents from FAISS vector database

2. Reranking
Computes cosine similarity between:
Query embedding
Document embeddings
Sorts documents by relevance

3. Filtering
Removes documents below a similarity threshold

4. Corrective Retrieval Loop 🔁
If no relevant documents found:
Reformulates query
Re-runs retrieval + reranking
Uses relaxed threshold

5. Context Generation
Combines filtered documents into final context

6. Answer Generation
Uses FLAN-T5 with strict prompt:
✅ Only answer from context
❌ No hallucination

7. Confidence Scoring
Based on semantic similarity:
🟢 HIGH
🟡 MEDIUM
🔴 LOW

8. Explainability Trace 🧾
Full pipeline logs displayed:
Retrieved docs
Reranked scores
Filtered results
Corrective steps

📊 Example Queries

Try:

Who founded Tesla?
Who created Microsoft?
What is Python used for?
Capital of France

📁 Project Structure
crag-pro-plus/
│
├── app.py              # Main Streamlit application
├── README.md           # Documentation
└── requirements.txt    # Dependencies (optional)

🎯 Design Principles
✅ Transparency First (Full trace visibility)
✅ Self-Correcting Retrieval
✅ Semantic Accuracy
✅ Low Hallucination Risk
✅ Deterministic Outputs

⚠️ Limitations
Small sample knowledge base (demo purpose)
No external data source integration
Single-user in-memory execution
Basic query reformulation logic

🛠️ Future Improvements
🌐 Integrate external knowledge sources (APIs / web)
🧠 Advanced reranking (Cross-Encoder models)
📊 Better confidence scoring metrics
🔍 Hybrid search (keyword + semantic)
☁️ Persistent vector database
🔐 Multi-user support & authentication
🤝 Contributing

Contributions are welcome!

Fork the repository
Create a feature branch
Submit a pull request
📄 License

This project is licensed under the MIT License.

🙌 Acknowledgements
Hugging Face for transformers & embeddings
FAISS for fast similarity search
Streamlit for rapid UI development
LangChain community modules