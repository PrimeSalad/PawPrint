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

# Configure Gemini (Mandatory for this version)
model_gemini = None
if GEMINI_API_KEY and GEMINI_API_KEY != "your_api_key_here":
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        # Use 1.5-flash for speed and low cost
        model_gemini = genai.GenerativeModel("gemini-1.5-flash")
        print("Gemini Vision configured.")
    except Exception as e:
        print(f"Gemini configuration failed: {e}")
        model_gemini = None
else:
    print("Warning: GEMINI_API_KEY not set. Gemini classification will fail.")


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
    """Use Gemini Vision to identify breed and get traits in one call."""
    if not model_gemini:
        return None

    prompt = """
    Analyze this image of a dog and identify its breed.
    Provide the following in JSON format:
    {
      "breed": "Name of the breed (e.g., Golden Retriever)",
      "confidence": 0.98,
      "description": {
        "short_desc": "A concise 2-sentence summary of the breed.",
        "traits": ["Trait 1", "Trait 2", "Trait 3"],
        "fun_fact": "An interesting fact about this breed."
      }
    }
    If the image is not a dog, return an error field in the JSON.
    Only return the JSON object, no other text.
    """

    try:
        # Prepare the image for Gemini
        img = Image.open(image_data).convert("RGB")
        
        response = model_gemini.generate_content([prompt, img])
        content = response.text.strip()

        # Clean JSON markdown if present
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()

        parsed = json.loads(content)
        
        if "error" in parsed:
            return {"error": parsed["error"]}
            
        return parsed
    except Exception as e:
        print(f"Gemini Vision error: {e}")
        return None


# -----------------------------
# ROUTES
# -----------------------------
@app.route("/")
def index():
    return "PawPrint Backend API (Gemini Powered) is running."


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "ok",
            "gemini_configured": model_gemini is not None,
            "engine": "Gemini 1.5 Flash (Vision Capability)"
        }
    )


@app.route("/predict", methods=["POST"])
def predict():
    try:
        if not model_gemini:
            return jsonify({"error": "Gemini AI not configured on server"}), 500

        if "image" not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        file = request.files["image"]

        if not file or file.filename == "":
            return jsonify({"error": "Empty file upload"}), 400

        # Perform Gemini Vision classification
        data = get_gemini_classification(file.stream)
        
        if not data:
            return jsonify({"error": "Failed to analyze image with AI"}), 500
            
        if "error" in data:
            return jsonify({"error": data["error"]}), 400

        # Map to the response format expected by the frontend
        results = [{
            "breed": data["breed"],
            "confidence": data.get("confidence", 0.95),
            "description": data["description"],
            "temp_file_name": file.filename
        }]

        # Cleanup memory
        gc.collect()

        return jsonify({"predictions": results})

    except Exception as e:
        print(f"Predict error: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/generate_pdf", methods=["POST"])
def generate_pdf():
    try:
        data = request.get_json(silent=True) or {}
        breed = data.get("breed", "Unknown Dog")

        report_text = f"Detailed report for {breed} is currently unavailable."

        if model_gemini:
            prompt = (
                f"Write a detailed, professional report about the dog breed: {breed}. "
                f"Include its history, general temperament, and basic care instructions. "
                f"Format it cleanly as plain text without markdown asterisks or hashes. "
                f"Limit to 3 or 4 paragraphs."
            )
            try:
                response = model_gemini.generate_content(prompt)
                report_text = response.text.replace("*", "").replace("#", "")
            except Exception as e:
                print(f"Gemini API error (fallback): {e}")
                report_text = f"Information about {breed} could not be generated at this time."

        pdf_filename = f"{breed.replace(' ', '_')}_report_{uuid.uuid4().hex[:8]}.pdf"
        reports_dir = os.path.join(app.static_folder, "reports")
        os.makedirs(reports_dir, exist_ok=True)
        pdf_path = os.path.join(reports_dir, pdf_filename)

        c = canvas.Canvas(pdf_path, pagesize=letter)
        width, height = letter

        # PDF background and layout (Keeping your professional styling)
        c.setFillColor(colors.HexColor("#faf8f6"))
        c.rect(0, 0, width, height, stroke=0, fill=1)
        c.setFillColor(colors.HexColor("#e26215"))
        c.rect(0, height - 15, width, 15, stroke=0, fill=1)

        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(colors.HexColor("#8a4f2a"))
        c.drawString(width - 240, height - 50, "AI BREED CLASSIFICATION")

        c.setFont("Helvetica", 10)
        c.setFillColor(colors.HexColor("#a08a7b"))
        c.drawString(width - 240, height - 65, f"Generated: {datetime.now().strftime('%B %d, %Y')}")

        c.setFillColor(colors.HexColor("#e26215"))
        c.roundRect(40, height - 160, width - 80, 50, 10, stroke=0, fill=1)

        c.setFont("Helvetica-Bold", 20)
        c.setFillColor(colors.white)
        c.drawString(60, height - 143, f"BREED REPORT: {breed.upper()}")

        c.setFont("Helvetica", 12)
        c.setFillColor(colors.HexColor("#7a3f1a"))
        text_object = c.beginText(50, height - 200)
        text_object.setLeading(20)

        for paragraph in report_text.split("\n"):
            if not paragraph.strip(): continue
            lines = textwrap.wrap(paragraph, width=80)
            for line in lines:
                if text_object.getY() < 100:
                    c.drawText(text_object)
                    c.showPage()
                    c.setFont("Helvetica", 12)
                    c.setFillColor(colors.HexColor("#7a3f1a"))
                    text_object = c.beginText(50, height - 50)
                    text_object.setLeading(20)
                text_object.textLine(line)
            text_object.textLine("")

        c.drawText(text_object)
        
        # Footer
        c.setFillColor(colors.HexColor("#1a0f08"))
        c.rect(0, 0, width, 60, stroke=0, fill=1)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(colors.HexColor("#e26215"))
        c.drawCentredString(width / 2.0, 35, "PAWPRINT AI")
        c.save()

        pdf_url = url_for("static", filename=f"reports/{pdf_filename}", _external=True)
        return jsonify({"pdf_url": pdf_url})

    except Exception as e:
        print(f"PDF error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=False)