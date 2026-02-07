from dotenv import load_dotenv
import os

load_dotenv()

from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)   # allows frontend to connect

# 🔑 PUT YOUR GEMINI API KEY HERE
genai.configure(api_key=os.getenv("AIzaSyBNGAuKd5iTTgabOTwAFvdh1YoSgsMzRfs"))

model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message")

    prompt = f"""
You are Gemini Shopping Copilot for India.
You help users compare prices across Blinkit, Zepto, Amazon, Zomato.
Give smart short helpful responses and recommendations.

User: {user_msg}
"""

    try:
        response = model.generate_content(prompt)
        reply = response.text
    except Exception as e:
        reply = "AI error: " + str(e)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
