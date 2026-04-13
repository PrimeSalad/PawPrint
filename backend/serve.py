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
        model_gemini = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config={
                "temperature": 0.4,
                "response_mime_type": "application/json",
            }
        )
        print("Gemini Vision (with Lens Fallback) configured.")
    except Exception as e:
        print(f"Gemini failed: {e}")
else:
    print("GEMINI_API_KEY missing.")


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
def get_gemini_classification(image_path):
    if not model_gemini:
        return None

    prompt = """
    Identify the dog breed. Return ONLY JSON:
    {"breed": "Name", "confidence": 0.9, "description": {"short_desc": "...", "traits": [], "fun_fact": "..."}}
    """

    try:
        img = Image.open(image_path).convert("RGB")
        img.thumbnail((800, 800))
        response = model_gemini.generate_content([prompt, img])
        if not response or not response.text:
            return None
        return json.loads(response.text)
    except Exception:
        return None


# -----------------------------
# ROUTES
# -----------------------------
@app.route("/")
def index():
    return jsonify({"status": "online", "fallback": "Google Lens Enabled"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image provided"}), 400

        file = request.files["image"]
        
        # SAVE IMAGE (Crucial for Lens fallback)
        ext = file.filename.split('.')[-1] if '.' in file.filename else 'jpg'
        filename = f"{uuid.uuid4().hex}.{ext}"
        upload_dir = os.path.join(app.static_folder, "uploads")
        os.makedirs(upload_dir, exist_ok=True)
        filepath = os.path.join(upload_dir, filename)
        file.save(filepath)
        
        # Public URL for the image
        image_url = url_for('static', filename=f'uploads/{filename}', _external=True)
        
        # TRY GEMINI
        data = get_gemini_classification(filepath)
        
        if not data:
            # FALLBACK TO LENS DATA
            # We provide the image URL so frontend can open Lens
            lens_url = f"https://lens.google.com/uploadbyurl?url={image_url}"
            return jsonify({
                "error": "AI classification blocked. Use Google Lens instead?",
                "fallback_url": lens_url,
                "image_url": image_url
            }), 200 # Return 200 so frontend can handle the UI

        results = [{
            "breed": data.get("breed", "Unknown"),
            "confidence": data.get("confidence", 0.9),
            "description": data.get("description", {}),
            "image_url": image_url
        }]

        gc.collect()
        return jsonify({"predictions": results})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
