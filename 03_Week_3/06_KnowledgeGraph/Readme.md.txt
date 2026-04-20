🛒 Product Knowledge Graph Explorer

An interactive Knowledge Graph + AI-powered explanation system built with Streamlit, NetworkX, and PyVis, enhanced with controlled LLM responses using Groq.

This project demonstrates how to combine structured data (graph-based truth) with LLM-generated insights, while minimizing hallucinations through strict constraints.

🚀 Features
🧠 Knowledge Graph-Based Retrieval
Uses NetworkX to model product relationships
Ensures results come from a trusted structured source
🔍 Query-Based Graph Exploration

Supports queries like:
"Show Apple products"
"Show mobile products"
"Show laptops"

📊 Interactive Graph Visualization
Built using PyVis
Highlights relevant nodes dynamically

🤖 Controlled AI Explanation
Uses Groq (LLaMA 3.1) for generating explanations
Strict prompt rules prevent hallucination

🛡️ Hallucination-Free Design
AI only explains results already present in the graph
No external or fabricated data allowed

🎨 Modern UI
Clean, dark-themed Streamlit interface

🏗️ Tech Stack
Python
Streamlit
NetworkX (Graph modeling)
PyVis (Graph visualization)
Groq API (LLaMA 3.1)

📦 Installation
Clone the repository:
git clone https://github.com/your-username/product-knowledge-graph.git
cd product-knowledge-graph

Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Install dependencies:
pip install streamlit networkx pyvis groq

🔐 Environment Setup

⚠️ Never hardcode API keys in production

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
1. Knowledge Graph Construction
Nodes represent:
Products (e.g., iPhone, MacBook)
Brands (Apple, Samsung)
Categories (Mobile, Laptop)
Edges define relationships:
Product → Brand
Product → Category

2. Query Processing
User input is matched against predefined categories:
Apple / Samsung
Mobile / Laptop
Relevant nodes are retrieved using graph traversal

3. Visualization
Graph is rendered using PyVis
Matching nodes are highlighted in green

4. Controlled AI Explanation
LLM receives:
Only the retrieved product list
User query

Prompt enforces:
❌ No new data
❌ No assumptions
✅ Only grounded explanations
📊 Example Queries

Try:

Show Apple products
Show Samsung products
Show mobile products
Show laptops

📁 Project Structure
product-knowledge-graph/
│
├── app.py          # Main Streamlit app
├── README.md       # Documentation
└── requirements.txt (optional)

⚠️ Design Principles
✅ Truth comes from Knowledge Graph
✅ LLM is only for explanation
✅ No hallucination allowed
✅ Deterministic outputs

🛠️ Future Improvements
🌐 Add dynamic graph data (database / API)
🧠 Expand ontology (more brands, categories, relationships)
🔎 Natural language query understanding
📊 Graph analytics (centrality, clustering)
☁️ Deploy on cloud platforms
🔐 Add authentication and user sessions
🤝 Contributing

Contributions are welcome!

Fork the repo
Create a feature branch
Submit a pull request

📄 License

This project is licensed under the MIT License.

🙌 Acknowledgements
NetworkX for graph modeling
PyVis for visualization
Groq for fast LLM inference
Streamlit for UI framework