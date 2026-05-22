import warnings
warnings.filterwarnings("ignore")

import google.generativeai as genai
import json

print("App started")

# Configure Gemini API
genai.configure(api_key="AIzaSyAr8qZj1A122qa8muXg2V_ZxKrUiMq2C4M")

# Load Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Input messages
messages = [
    "My payment got deducted but service is not activated",
    "App crashes every time I login",
    "How to change my email address?"
]

results = []

# Process each message
for msg in messages:

    print("Processing:", msg)

    prompt = f"""
You are a support ticket classifier.

Classify the given message into:

Categories:
- Billing
- Technical Issue
- Account
- General Inquiry

Priority Levels:
- High
- Medium
- Low

Return ONLY valid JSON:

{{
  "category": "",
  "priority": ""
}}

Message: "{msg}"
"""

    try:
        # AI response
        response = model.generate_content(prompt)

        output = response.text.strip()

        print("AI Output:", output)

        parsed = json.loads(output)

    except Exception as e:

        print("API Error:", e)
        print("Using mock response instead...")

        # Mock fallback response
        if "payment" in msg.lower():
            parsed = {
                "category": "Billing",
                "priority": "High"
            }

        elif "crash" in msg.lower() or "login" in msg.lower():
            parsed = {
                "category": "Technical Issue",
                "priority": "High"
            }

        elif "email" in msg.lower():
            parsed = {
                "category": "Account",
                "priority": "Low"
            }

        else:
            parsed = {
                "category": "General Inquiry",
                "priority": "Low"
            }

    # Append final structured output
    results.append({
        "message": msg,
        "category": parsed["category"],
        "priority": parsed["priority"]
    })

# Print final JSON output
print("\nFinal Output:\n")

print(json.dumps(results, indent=2))

# Save output to file
with open("sample_output.json", "w") as file:
    json.dump(results, file, indent=2)

print("\nOutput saved to sample_output.json")
