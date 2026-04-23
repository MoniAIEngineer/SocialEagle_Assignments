# AI Excel Data Cleaner

A GenAI-assisted Excel data cleaning and audit tool built with Streamlit.

This project helps clean messy Excel files by combining:
- **rule-based data cleaning**
- **prompt-based GenAI suggestions**
- **auditable before/after summaries**

It is designed for real-world Excel cleanup tasks in data migration, operations, QA, and reporting workflows.

---

## Features

### Core Cleaning Features
- Remove exact duplicate rows
- Remove key-based duplicates using selected columns
- Normalize null-like values such as:
  - `N/A`
  - `NA`
  - `null`
  - `-`
  - empty strings
- Fill missing values intelligently
- Drop rows with nulls if needed
- Trim leading and trailing whitespace
- Standardize text case for names, cities, and similar columns
- Standardize email format
- Standardize phone numbers
- Standardize mixed date formats
- Convert numeric-like text to numeric values
- Detect invalid emails
- Detect invalid dates

### Audit and Reporting Features
- Before/after row counts
- Duplicate removal count
- Null values filled count
- Trimmed cell count
- Date standardized count
- Phone standardized count
- Email standardized count
- Invalid email report
- Invalid date report
- Before/after data profile
- Download cleaned sheet as CSV
- Download cleaned workbook as Excel

### GenAI Features
- Prompt-based data quality suggestions
- Likely column type suggestions
- Duplicate risk suggestions
- Validation rule suggestions
- Cleaning recommendations for uploaded spreadsheet preview

---

## Why this is a GenAI Project

This is a **GenAI-assisted** project.

The tool uses a prompt-driven LLM to:
- inspect spreadsheet previews
- suggest data quality issues
- infer likely column types
- recommend validation rules
- recommend cleaning actions

The actual cleaning is then done programmatically for:
- reliability
- traceability
- exact counting
- safe file export

This hybrid approach is practical and realistic for real-world projects.

---

## Project File Name

Use this Python file name:

```python
ai_excel_data_cleaner_app.py
```

---

## Installation

### 1. Create a virtual environment (recommended)

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements_excel_cleaner.txt
```

---

## Run the App

```bash
streamlit run ai_excel_data_cleaner_app.py
```

---

## OpenAI API Key Setup

This project works **without API key** for the core cleaning engine.

If you want the **GenAI Suggestions** feature, provide an OpenAI API key.

### Option 1: Hardcoded key for local testing
Inside the script:

```python
HARDCODED_OPENAI_API_KEY = "your_api_key_here"
```

### Option 2: Environment variable

#### Windows PowerShell
```bash
setx OPENAI_API_KEY "your_api_key_here"
```

Restart terminal after setting it.

#### macOS / Linux
```bash
export OPENAI_API_KEY="your_api_key_here"
```

### Option 3: Streamlit secrets

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
OPENAI_API_KEY = "your_api_key_here"
```

---

## Supported Input

- Excel `.xlsx`
- Excel `.xls`

---

## Supported Output

- Cleaned selected sheet as CSV
- Cleaned workbook as Excel
- Audit report table
- Invalid email review table
- Invalid date review table
- Before/after data profile
- GenAI suggestions report

---

## Cleaning Scenarios Covered

This project handles:

1. Duplicate rows copied during manual consolidation
2. Blank cells represented as `N/A`, `NA`, `-`, `null`, or empty strings
3. Dates stored in mixed formats like:
   - `01/02/2024`
   - `2024-02-01`
   - `Feb 1 2024`
4. Emails with uppercase letters or leading/trailing spaces
5. Phone numbers with spaces, plus signs, dashes, or brackets
6. Names and city values with inconsistent capitalization
7. Numeric columns stored as text because of commas or percent signs
8. Rows with partially missing values
9. Invalid date values that cannot be parsed
10. Invalid email values that need manual review

---

## Recommended Test Settings

For sample files, try:

### Run 1
- Null handling strategy: `Fill nulls intelligently`
- Duplicate handling strategy: `Remove exact duplicates`

### Run 2
- Null handling strategy: `Fill nulls intelligently`
- Duplicate handling strategy: `Remove duplicates based on selected keys`

Suggested key columns:
- `Record_ID`
- `Email`
- `Phone`

---

## Example Output Metrics

The app can show metrics like:

- Rows Before
- Rows After
- Duplicate Rows Removed
- Null Values Filled
- Trimmed Cells
- Date Cells Standardized
- Phone Cells Standardized
- Email Cells Standardized

This makes the tool auditable and useful in real project environments.

---

## Resume Description

Built a GenAI-assisted Excel data cleaning and audit tool using Streamlit, pandas, and prompt-based LLM suggestions to detect and fix duplicates, null values, formatting inconsistencies, invalid emails, invalid dates, and numeric text issues while generating detailed audit counts and downloadable cleaned files.

---

## Interview Explanation

You can describe it like this:

> This is a GenAI-assisted Excel data cleaner that combines prompt-based LLM suggestions with rule-based cleaning logic. The AI helps identify quality issues and recommend validation rules, while the cleaning engine performs reliable transformations and produces an auditable summary of all updates.

---

## Future Improvements

- AI-based automatic column classification
- Data quality score
- Row-level anomaly explanations
- Business-rule validation suggestions
- Charts for before vs after quality comparison
- Support for CSV uploads
- Multi-sheet batch cleaning
