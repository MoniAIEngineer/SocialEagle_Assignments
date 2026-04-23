# AI SQL Tutor App 🚀

A GenAI-powered **Chat-to-SQL Generator and SQL Explainer** built using Streamlit.

This tool converts natural language questions into SQL queries and explains them step-by-step using sample tables.

---

## 🔥 Features

### 🤖 GenAI Features
- Convert plain English questions into SQL queries
- Uses prompt-based LLM (OpenAI)
- Explains SQL queries step-by-step
- Helps beginners understand SQL logic

### 🧠 SQL Learning Features
- Covers **basic to advanced SQL**
- Step-by-step execution explanation:
  - FROM
  - JOIN
  - WHERE
  - GROUP BY
  - HAVING
  - SELECT
  - ORDER BY

### 📊 Sample Database
Includes example tables like:
- `customers`
- `orders`

Used for:
- query generation
- explanation walkthrough

---

## 🏗️ Project Structure

```text
ai_sql_tutor_app.py
requirements.txt
README.md
⚙️ Installation
1. Create Virtual Environment (optional)
Windows
python -m venv venv
venv\Scripts\activate
Mac/Linux
python3 -m venv venv
source venv/bin/activate
2. Install Dependencies
pip install -r requirements.txt
▶️ Run the App
streamlit run ai_sql_tutor_app.py
🔑 OpenAI API Setup

This project requires an OpenAI API key for SQL generation.

Option 1: Hardcode (for testing)
OPENAI_API_KEY = "your_api_key_here"
Option 2: Environment Variable
Windows
setx OPENAI_API_KEY "your_api_key_here"
Mac/Linux
export OPENAI_API_KEY="your_api_key_here"
Option 3: Streamlit Secrets

Create file:

.streamlit/secrets.toml

Add:

OPENAI_API_KEY = "your_api_key_here"
💡 Example Questions to Test
🟢 Basic Queries
Show all customers
List all orders
Show customers from New York
🟡 Intermediate Queries
Show total orders per customer
List customers with more than 2 orders
Show orders placed this month
🔴 Advanced Queries
Which users bought the most?
Top 5 customers by total spending
Customers who never placed an order
Monthly revenue trend
Rank customers by purchase amount
🧪 What This Project Demonstrates
Prompt engineering
GenAI + SQL integration
Natural language to database query conversion
SQL teaching through explanation
Real-world use case (data analytics assistant)
📈 Why This Is a High-Impact Project
Reduces effort for non-technical users
Helps beginners learn SQL interactively
Can be used in real companies for:
data analysis
reporting
business insights
Demonstrates both GenAI + backend logic
🧠 How It Works
User enters a question in plain English
Prompt is sent to LLM
LLM generates SQL query
Query is displayed
App explains:
how query runs
what each clause does
Uses sample data for demonstration
🧩 Future Enhancements
Connect to real databases (MySQL, PostgreSQL)
Execute SQL and show results
Add query optimization suggestions
Add chart visualizations
Add error correction for bad queries

✅ Summary

This is a GenAI-powered SQL assistant + learning tool that:

generates queries
explains logic
improves productivity
helps users learn SQL
