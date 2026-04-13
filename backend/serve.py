import os
import json
import uuid
import textwrap
import gc
from datetime import datetime

from flask import Flask, request, jsonify, url_for, make_response
from flask_cors import CORS
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# -----------------------------
# LOAD ENVIRONMENT VARIABLES
# -----------------------------
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PORT = int(os.getenv("PORT", 5000))

# Configure Gemini
model_gemini = None
if GEMINI_API_KEY and GEMINI_API_KEY != "your_api_key_here":
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model_gemini = genai.GenerativeModel("gemini-1.5-flash")
        print("Gemini Vision configured.")
    except Exception as e:
        print(f"Gemini configuration failed: {e}")
else:
    print("CRITICAL: GEMINI_API_KEY is not set!")


# -----------------------------
# FLASK APP & CORS
# -----------------------------
app = Flask(__name__, static_folder="static")

@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

CORS(app)


# -----------------------------
# HELPERS
# -----------------------------
def get_gemini_classification(image_data):
    if not model_gemini:
        return {"error": "Gemini API Key missing on server."}

    prompt = """
    Analyze this image of a dog and identify its breed.
    Return ONLY a JSON object:
    {
      "breed": "Breed Name",
      "confidence": 0.95,
      "description": {
        "short_desc": "2-sentence summary.",
        "traits": ["Trait 1", "Trait 2", "Trait 3"],
        "fun_fact": "One fun fact."
      }
    }
    """

    try:
        img = Image.open(image_data).convert("RGB")
        response = model_gemini.generate_content([prompt, img])
        
        content = response.text.strip()
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()

        return json.loads(content)
    except Exception as e:
        print(f"Gemini Error: {e}")
        return None


# -----------------------------
# ROUTES
# -----------------------------
@app.route("/")
def index():
    return jsonify({"status": "online", "engine": "Gemini Flash"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image provided"}), 400

        file = request.files["image"]
        data = get_gemini_classification(file.stream)
        
        if not data or "error" in data:
            return jsonify({"error": data.get("error") if data else "AI Analysis failed"}), 500

        results = [{
            "breed": data["breed"],
            "confidence": data.get("confidence", 0.95),
            "description": data["description"],
            "temp_file_name": file.filename
        }]

        gc.collect()
        return jsonify({"predictions": results})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/generate_pdf", methods=["POST"])
def generate_pdf():
    try:
        data = request.get_json() or {}
        breed = data.get("breed", "Unknown Dog")
        
        pdf_filename = f"report_{uuid.uuid4().hex[:8]}.pdf"
        reports_dir = os.path.join(app.static_folder, "reports")
        os.makedirs(reports_dir, exist_ok=True)
        pdf_path = os.path.join(reports_dir, pdf_filename)

        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.setFont("Helvetica-Bold", 20)
        c.drawString(100, 700, f"BREED REPORT: {breed.upper()}")
        c.save()

        return jsonify({"pdf_url": url_for("static", filename=f"reports/{pdf_filename}", _external=True)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
