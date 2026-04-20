🌐 Multi-Page Website Chatbot

An intelligent AI-powered chatbot that can crawl an entire website, extract its content, and allow users to ask questions based strictly on that website’s data.

Built using Streamlit, LangChain, Hugging Face embeddings, and Groq LLM, this project demonstrates a practical RAG (Retrieval-Augmented Generation) pipeline with live web crawling.

🚀 Features
🕷️ Multi-Page Website Crawling
Automatically crawls internal links within a domain
Extracts clean textual content from multiple pages

🧠 Semantic Search with Embeddings
Uses Hugging Face transformer embeddings
Stores content in a Chroma vector database

💬 Chat-Based Interface
Ask questions naturally about the website
Maintains chat history

🎯 Context-Grounded Answers
LLM answers strictly from retrieved content
Prevents hallucination with constrained prompts

🔍 Debug Mode
View retrieved context for transparency
⚡ Fast & Lightweight
In-memory vector database
Cached embeddings for performance

🏗️ Tech Stack
Python
Streamlit
Requests + BeautifulSoup (Web scraping)
LangChain
Hugging Face Embeddings
Chroma Vector Store
Groq (LLaMA 3.1)

📦 Installation
Clone the repository:
git clone https://github.com/your-username/website-chatbot.git
cd website-chatbot

Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

Install dependencies:
pip install streamlit requests beautifulsoup4 langchain langchain-huggingface langchain-chroma groq

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
1. Website Crawling
Starts from a given URL
Crawls internal links (same domain only)
Limits pages (default: 10)

Removes unwanted HTML elements:
scripts
styles
navigation
footer

2. Text Processing
Extracted text is:
Cleaned
Combined

Split into chunks using:

RecursiveCharacterTextSplitter

3. Vector Database
Chunks are converted into embeddings
Stored in Chroma vector store
Enables fast semantic retrieval

4. Question Answering (RAG)

When a user asks a question:

Relevant chunks are retrieved
Context is passed to LLM
LLM generates answer only from context

5. Hallucination Control

Prompt enforces:

✅ Answer only from context
❌ No guessing
❌ No external knowledge

Fallback response:

"I don't find this in the website."
📊 Example Use Cases

Try with:

Documentation websites
Product documentation portals
Blogs or knowledge bases

Example queries:

What is Python list?
Explain functions in Python
What is this page about?

📁 Project Structure
website-chatbot/
│
├── app.py              # Main Streamlit application
├── README.md           # Documentation
└── requirements.txt    # Dependencies (optional)

⚠️ Limitations
Limited to a fixed number of pages (default: 10)
No JavaScript-rendered content (static HTML only)
May miss deeply nested pages
Depends on website structure and accessibility

🛠️ Future Improvements
🌐 Support dynamic content (Playwright / Selenium)
📊 Add source citations in answers
🧠 Improve ranking with hybrid search
☁️ Persist vector database
🔐 Add authentication
🚀 Deploy on cloud platforms
🤝 Contributing

Contributions are welcome!

Fork the repo
Create a feature branch
Submit a pull request

📄 License

This project is licensed under the MIT License.

🙌 Acknowledgements
Hugging Face for embeddings
LangChain for RAG framework
Groq for fast LLM inference
Streamlit for UI
BeautifulSoup for web scraping