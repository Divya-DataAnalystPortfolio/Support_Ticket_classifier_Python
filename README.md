# AI Support Ticket Classifier

## Project Overview

This project demonstrates an AI-powered support ticket classification workflow using Python and Google Gemini API integration.

Customer support teams receive large volumes of support messages daily. Manually categorizing and prioritizing these tickets can be time-consuming and inefficient.

This solution automates:
- Ticket classification
- Priority assignment
- Structured JSON output generation

---

# Features

- Accepts multiple customer support messages
- Uses AI-based classification workflow
- Assigns:
  - Category
  - Priority
- Returns structured JSON output
- Includes fallback mock responses for API quota limitations

---

# Categories

The application classifies messages into the following categories:

- Billing
- Technical Issue
- Account
- General Inquiry

---

# Priority Levels

| Priority | Description |
|---|---|
| High | Urgent or blocking issues |
| Medium | Moderate issues |
| Low | General or informational queries |

---

# Technologies Used

- Python
- Google Gemini API
- JSON

---

# Project Structure

```bash
support-ticket-classifier/
│
├── app.py
├── requirements.txt
├── sample_output.json
└── README.md
```

# API Setup

This project is designed using Google Gemini API integration.

Generate API key from:

https://aistudio.google.com/app/apikey

Replace API key inside `app.py`:

```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

---

# How to Run

```bash
python app.py
```

OR run using Python IDLE:
- Open `app.py`
- Press `F5`

---

# Input Example

```python
messages = [
    "My payment got deducted but service is not activated",
    "App crashes every time I login",
    "How to change my email address?"
]
```

---

# Sample Output

```json
[
  {
    "message": "My payment got deducted but service is not activated",
    "category": "Billing",
    "priority": "High"
  },
  {
    "message": "App crashes every time I login",
    "category": "Technical Issue",
    "priority": "High"
  },
  {
    "message": "How to change my email address?",
    "category": "Account",
    "priority": "Low"
  }
]
```

---

# Workflow

```text
Customer Messages
        ↓
Python Application
        ↓
Gemini API / Mock Fallback
        ↓
Ticket Classification
        ↓
Structured JSON Output
```

---

# Error Handling

The application includes:
- API exception handling
- Fallback mock classification logic
- JSON parsing support

This allows the project to continue functioning even if API quota limitations occur.

---

# Future Enhancements

Possible improvements:
- CSV file input support
- Streamlit web application
- SQL database integration
- Power BI dashboard
- Sentiment analysis
- Automatic ticket routing

---

# Learning Outcomes

This project demonstrates:
- Python programming
- API integration
- AI workflow understanding
- JSON handling
- Prompt engineering
- Exception handling
- Automation concepts

---

# Note

Google Gemini API was used as a free alternative to OpenAI API for demonstrating the AI-based support ticket classification workflow.
