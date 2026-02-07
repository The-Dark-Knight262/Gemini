import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(user_msg):
    prompt = f"""
You are Gemini Shopping Copilot for India.
Compare prices across Blinkit, Zepto, Amazon, Zomato.
Give short smart helpful recommendation.

User: {user_msg}
"""

    response = model.generate_content(prompt)
    return response.text
