🛒 Smart Product Search

A simple and interactive AI-powered product search app built using Streamlit, LangChain, and Hugging Face embeddings.
This project demonstrates how semantic search can be used to find relevant products based on user queries.

🚀 Features
🔍 Semantic Search using transformer-based embeddings
⚡ Fast in-memory vector search with Chroma
🧠 Uses Hugging Face sentence-transformers model
🎯 Returns top relevant product matches
🧹 Removes duplicate search results

💻 Simple and clean Streamlit UI

🏗️ Tech Stack
Python
Streamlit
LangChain
Hugging Face Embeddings
Chroma Vector Store

📦 Installation

Clone the repository:
git clone https://github.com/your-username/smart-product-search.git
cd smart-product-search

Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

Install dependencies:
pip install streamlit langchain langchain-huggingface chromadb
▶️ Running the App
streamlit run app.py

The app will open in your browser at:

http://localhost:8501

🧠 How It Works
A list of predefined product descriptions is created.

These descriptions are converted into vector embeddings using:

sentence-transformers/all-MiniLM-L6-v2
The embeddings are stored in an in-memory Chroma vector database.
When a user enters a query:
The query is converted into an embedding
Similarity search is performed
Top matching products are retrieved
Duplicate results are filtered out before display.

📊 Example Queries

Try searching for:

best phone for photography
cheap mobile
gaming computer
office laptop
camera for professionals

📁 Project Structure
smart-product-search/
│
├── app.py          # Main Streamlit application
├── README.md       # Project documentation
└── requirements.txt (optional)

🛠️ Future Improvements
🔗 Connect to real product databases (e-commerce APIs)
🧾 Add product metadata (price, ratings, links)
🧠 Improve ranking with hybrid search (keyword + semantic)
🌐 Deploy on Streamlit Cloud / Docker
🗂️ Persist vector database instead of in-memory storage