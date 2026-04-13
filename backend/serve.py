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
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# -----------------------------
# LOAD ENVIRONMENT VARIABLES
# -----------------------------
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PORT = int(os.getenv("PORT", 5000))

# Configure Gemini for Free Tier
model_gemini = None
if GEMINI_API_KEY and GEMINI_API_KEY != "your_api_key_here":
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        # Use BLOCK_ONLY_HIGH for Free Tier compatibility
        model_gemini = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            safety_settings={
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            }
        )
        print("Gemini Vision configured for Free Tier.")
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

    # Simplified prompt to avoid triggering safety filters
    prompt = """
    Instruction: Classify the dog breed in the photo. 
    Output must be a single JSON object with: 
    "breed", "confidence" (0.0-1.0), and "description" (object with "short_desc", "traits" list, "fun_fact").
    """

    try:
        img = Image.open(image_data).convert("RGB")
        # Resize image to save bandwidth/tokens on Free Tier
        img.thumbnail((800, 800)) 
        
        response = model_gemini.generate_content([prompt, img])
        
        if not response or not response.text:
            print("Gemini Error: Safety filters might have blocked this.")
            return None

        content = response.text.strip()
        # Clean JSON
        if "{" in content:
            content = content[content.find("{"):content.rfind("}")+1]
        
        return json.loads(content)
    except Exception as e:
        print(f"Gemini AI Error: {e}")
        return None


# -----------------------------
# ROUTES
# -----------------------------
@app.route("/")
def index():
    return jsonify({"status": "online", "mode": "Free Tier Optimized"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image provided"}), 400

        file = request.files["image"]
        data = get_gemini_classification(file.stream)
        
        if not data:
            return jsonify({"error": "AI could not identify the dog. Please use a clearer photo."}), 500

        results = [{
            "breed": data.get("breed", "Unknown"),
            "confidence": data.get("confidence", 0.9),
            "description": data.get("description", {
                "short_desc": "Information not available.",
                "traits": ["Loyal"],
                "fun_fact": "N/A"
            }),
            "temp_file_name": file.filename
        }]

        gc.collect()
        return jsonify({"predictions": results})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/generate_pdf", methods=["POST"])
def generate_pdf():
    # Simple PDF generation to keep it lightweight
    try:
        data = request.get_json() or {}
        breed = data.get("breed", "Unknown Dog")
        
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
        
        pdf_filename = f"report_{uuid.uuid4().hex[:8]}.pdf"
        reports_dir = os.path.join(app.static_folder, "reports")
        os.makedirs(reports_dir, exist_ok=True)
        pdf_path = os.path.join(reports_dir, pdf_filename)

        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.drawString(100, 750, f"PawPrint AI Breed Report: {breed}")
        c.save()

        return jsonify({"pdf_url": url_for("static", filename=f"reports/{pdf_filename}", _external=True)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
