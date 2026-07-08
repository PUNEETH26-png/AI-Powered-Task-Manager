import google.generativeai as genai
import json
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")




def suggest_task(prompt: str):

    system_prompt = f"""
You are a task generation assistant.

Return ONLY a valid JSON object.

Do not use markdown.
Do not use ```json.
Do not add explanations.

The response must have exactly this format:

{{
    "title": "",
    "description": "",
    "priority": "Low"
}}

Priority must be exactly one of:
- Low
- Medium
- High

User Request:
{prompt}
"""

    response = model.generate_content(system_prompt)

    text = response.text.strip()

    # Remove markdown if Gemini still returns it
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    try:
        return json.loads(text)

    except json.JSONDecodeError:
        raise Exception(
            f"Gemini did not return valid JSON.\n\nResponse:\n{text}"
        )