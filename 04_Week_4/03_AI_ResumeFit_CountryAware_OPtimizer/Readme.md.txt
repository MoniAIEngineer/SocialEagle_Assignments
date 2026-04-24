📄 ResumeFit AI – Country-Aware Resume Optimizer
🚀 Overview

ResumeFit AI is a GenAI-powered application that helps users evaluate and optimize their resumes for a specific job role and country.

It analyzes how well your resume matches a job description, identifies keyword gaps, validates missing experience, and rewrites your resume to improve your chances of getting shortlisted — all while adapting to country-specific resume formats (India, Germany, USA, UK, Canada, etc.).

🎯 Key Features
✅ Resume Fit Analysis
Calculates match percentage between your resume and job description
Extracts:
Matched keywords
Missing keywords
Skill gaps
Provides section-wise feedback
🌍 Country-Aware Resume Formatting
Adapts resume structure based on selected country:
🇮🇳 India → Skills + Projects focused
🇩🇪 Germany → Formal, structured CV
🇺🇸 USA → Impact-driven, ATS-optimized
🇬🇧 UK → Balanced CV style
🇨🇦 Canada → Skills + achievements focus
Shows:
✅ Recommended section order
✅ Sample resume template
📊 Format Verification Engine
Checks if your resume follows country-specific standards
Outputs:
✔ Section order match status
✔ Template format match
✔ Missing sections / structure issues
✔ Clear improvement suggestions
❓ Gap Validation (Smart AI Questions)
Generates targeted questions for missing skills/experience
User confirms what can be added
Prevents fake or hallucinated resume updates
✍️ AI Resume Rewriter
Enhances resume using:
Job description alignment
Confirmed user inputs
Country-specific formatting rules
Generates:
New bullet points
Improved resume structure
ATS-friendly content
📈 Re-Scoring
Calculates new fit percentage after update
Shows improvement clearly
📥 Export
Download optimized resume as DOCX file
🧠 Tech Stack
Frontend/UI: Streamlit
LLM Orchestration: LangChain
LLM Provider: OpenAI (GPT-4o-mini)
Document Processing:
PDF → pypdf
DOCX → python-docx
Environment Handling: python-dotenv
📦 Installation
pip install streamlit langchain langchain-openai openai pypdf python-docx python-dotenv
🔑 Setup API Key

Create a .env file:

OPENAI_API_KEY=your_api_key_here

Or hardcode (for testing only):

os.environ["OPENAI_API_KEY"] = "your_api_key_here"
▶️ Run the App
streamlit run App.py
🧭 How It Works
Select target country
Upload resume (PDF/DOCX/TXT)
Paste job description
Click Analyze Resume Fit
Review:
Fit score
Keywords
Gaps
Format validation
Answer AI-generated gap questions
Click Update Resume
Download optimized resume
📌 Project Highlights
Combines ATS optimization + GenAI rewriting
Prevents fake content via user validation loop
Supports multi-country resume standards
Uses structured LLM outputs (LangChain) instead of plain text

End-to-end pipeline:

Resume → Analysis → Gap Detection → User Validation → Rewrite → Re-score
🔮 Future Enhancements
📄 Export to country-specific DOCX templates (styled)
🧠 Add RAG for industry-specific keyword intelligence
📊 ATS simulation scoring engine
🌐 Multi-language resume support
☁️ Deployment (Streamlit Cloud / AWS / Azure)
⚠️ Disclaimer
The tool does not fabricate experience
Resume improvements are based only on:
Existing content
User-confirmed inputs