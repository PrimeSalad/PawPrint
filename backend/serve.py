import os
import json
import uuid
import textwrap
from datetime import datetime

from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from dotenv import load_dotenv
from PIL import Image
import numpy as np
import tensorflow as tf
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

# Configure Gemini if available
model_gemini = None
if GEMINI_API_KEY and GEMINI_API_KEY != "your_api_key_here":
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model_gemini = genai.GenerativeModel("gemini-2.5-flash")
        print("Gemini configured.")
    except Exception as e:
        print(f"Gemini configuration failed: {e}")
        model_gemini = None
else:
    print("Warning: GEMINI_API_KEY not set. Using fallback descriptions.")


# -----------------------------
# FLASK APP
# -----------------------------
app = Flask(__name__, static_folder="static")

# Professional CORS Configuration
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})


# -----------------------------
# MODEL CONFIG
# -----------------------------
IMG_SIZE = 224
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "dog_model")
LABELS_PATH = os.path.join(BASE_DIR, "labels.json")

model = None
infer = None
idx_to_class = {}

print("Loading model...")
try:
    model = tf.saved_model.load(MODEL_PATH)
    infer = model.signatures["serving_default"]
    print("Model loaded.")
except Exception as e:
    print(f"Model load failed: {e}")
    model = None
    infer = None

print("Loading labels...")
try:
    with open(LABELS_PATH, "r", encoding="utf-8") as f:
        class_indices = json.load(f)
    idx_to_class = {v: k for k, v in class_indices.items()}
    print("Labels loaded.")
except Exception as e:
    print(f"Labels load failed: {e}")
    idx_to_class = {}


# -----------------------------
# HELPERS
# -----------------------------
def preprocess_image(image_stream):
    img = Image.open(image_stream).convert("RGB")
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img_array = np.array(img).astype(np.float32) / 255.0
    return np.expand_dims(img_array, axis=0)


def get_gemini_info_sync(breed):
    if not model_gemini:
        return {
            "short_desc": f"The {breed} is a wonderful and unique breed known for its distinctive features.",
            "traits": ["Loyal", "Energetic", "Friendly"],
            "fun_fact": f"The {breed} has a rich history and makes a great companion.",
        }

    prompt = f"""
    Provide a concise and engaging description for the dog breed: {breed}.
    Include:
    1. A short summary (2 sentences).
    2. Key traits (3-4 bullet points).
    3. Fun fact.
    Format the response as JSON with keys: "short_desc", "traits", "fun_fact".
    """

    try:
        response = model_gemini.generate_content(prompt)
        content = response.text.strip()

        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()

        parsed = json.loads(content)

        return {
            "short_desc": parsed.get(
                "short_desc",
                f"The {breed} is known for its distinctive features and loyal nature.",
            ),
            "traits": parsed.get("traits", ["Loyal", "Energetic", "Intelligent"]),
            "fun_fact": parsed.get(
                "fun_fact",
                "This breed has a rich history as a companion dog.",
            ),
        }
    except Exception as e:
        print(f"Gemini error for {breed}: {e}")
        return {
            "short_desc": f"The {breed} is known for its distinctive features and loyal nature.",
            "traits": ["Loyal", "Energetic", "Intelligent"],
            "fun_fact": "This breed has a rich history as a companion dog.",
        }


# -----------------------------
# ROUTES
# -----------------------------
@app.route("/")
def index():
    return "PawPrint Backend API is running."


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "ok",
            "model_loaded": infer is not None,
            "labels_loaded": bool(idx_to_class),
            "gemini_configured": model_gemini is not None,
        }
    )


@app.route("/predict", methods=["POST"])
def predict():
    try:
        if infer is None:
            return jsonify({"error": "Model not available on server"}), 500

        if not idx_to_class:
            return jsonify({"error": "Labels not available on server"}), 500

        if "image" not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        file = request.files["image"]

        if not file or file.filename == "":
            return jsonify({"error": "Empty file upload"}), 400

        x = preprocess_image(file.stream)

        preds_dict = infer(tf.constant(x))
        preds = list(preds_dict.values())[0].numpy()[0]

        top_indices = preds.argsort()[-1:][::-1]

        results = []
        for idx in top_indices:
            breed = idx_to_class.get(int(idx), "Unknown Breed")
            conf = float(preds[int(idx)])
            description = get_gemini_info_sync(breed)

            results.append(
                {
                    "breed": breed,
                    "confidence": conf,
                    "description": description,
                    "temp_file_name": file.filename,
                }
            )

        return jsonify({"predictions": results})

    except Exception as e:
        print(f"Predict error: {e}")
        return jsonify({"error": str(e)}), 500


@app.route("/generate_pdf", methods=["POST"])
def generate_pdf():
    try:
        data = request.get_json(silent=True) or {}
        breed = data.get("breed", "Unknown Dog")

        report_text = f"Detailed report for {breed} is currently unavailable as Gemini is not configured."

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
                print(f"Gemini API error (fallback triggered): {e}")
                report_text = (
                    f"HISTORY\n"
                    f"The {breed} is a wonderful and widely recognized canine breed with a fascinating history. "
                    f"Originally bred for specific working or companionship purposes, they have adapted over the years "
                    f"into loving household pets. Their distinct lineage gives them unique physical and behavioral traits "
                    f"that set them apart from other breeds.\n\n"
                    f"TEMPERAMENT\n"
                    f"In terms of temperament, the {breed} is generally known to be highly loyal, energetic, and "
                    f"affectionate with their families. They typically form strong bonds with their owners and thrive "
                    f"on daily interaction. While individual personalities can vary, most display a keen intelligence "
                    f"and an eagerness to learn, making them highly responsive to consistent positive reinforcement.\n\n"
                    f"CARE & EXERCISE\n"
                    f"When caring for a {breed}, it is essential to provide them with adequate physical and mental "
                    f"stimulation. Daily exercise, such as brisk walks or interactive play, helps prevent boredom and "
                    f"keeps them physically fit. Routine grooming, a balanced diet, and regular veterinary check-ups "
                    f"are also necessary to ensure a long, healthy, and happy life for your companion."
                )

        pdf_filename = f"{breed.replace(' ', '_')}_report_{uuid.uuid4().hex[:8]}.pdf"
        reports_dir = os.path.join(app.static_folder, "reports")
        os.makedirs(reports_dir, exist_ok=True)
        pdf_path = os.path.join(reports_dir, pdf_filename)

        c = canvas.Canvas(pdf_path, pagesize=letter)
        width, height = letter

        c.setFillColor(colors.HexColor("#faf8f6"))
        c.rect(0, 0, width, height, stroke=0, fill=1)

        c.setFillColor(colors.HexColor("#e26215"))
        c.rect(0, height - 15, width, 15, stroke=0, fill=1)

        logo_path = os.path.join(BASE_DIR, "..", "frontend", "images", "logo.png")
        if os.path.exists(logo_path):
            try:
                c.drawImage(
                    logo_path,
                    40,
                    height - 85,
                    width=160,
                    preserveAspectRatio=True,
                    mask="auto",
                )
            except Exception as img_err:
                print(f"Logo draw error: {img_err}")

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
            if not paragraph.strip():
                continue

            if paragraph.isupper() or paragraph.startswith("**"):
                c.drawText(text_object)
                c.setFont("Helvetica-Bold", 14)
                c.setFillColor(colors.HexColor("#e26215"))
                text_object = c.beginText(50, text_object.getY() - 10)
                text_object.setLeading(20)
                paragraph = paragraph.replace("**", "")
                text_object.textLine(paragraph)
                c.drawText(text_object)
                c.setFont("Helvetica", 12)
                c.setFillColor(colors.HexColor("#7a3f1a"))
                text_object = c.beginText(50, text_object.getY() - 5)
                text_object.setLeading(20)
                continue

            lines = textwrap.wrap(paragraph.replace("**", ""), width=80)
            for line in lines:
                if text_object.getY() < 100:
                    c.drawText(text_object)
                    c.showPage()

                    c.setFillColor(colors.HexColor("#faf8f6"))
                    c.rect(0, 0, width, height, stroke=0, fill=1)

                    c.setFont("Helvetica", 12)
                    c.setFillColor(colors.HexColor("#7a3f1a"))
                    text_object = c.beginText(50, height - 50)
                    text_object.setLeading(20)

                text_object.textLine(line)

            text_object.textLine("")

        c.drawText(text_object)

        c.setFillColor(colors.HexColor("#1a0f08"))
        c.rect(0, 0, width, 60, stroke=0, fill=1)

        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(colors.HexColor("#e26215"))
        c.drawCentredString(width / 2.0, 35, "PAWPRINT AI")

        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor("#8a7563"))
        c.drawCentredString(
            width / 2.0,
            20,
            "Identifying stories, one pawprint at a time. | © 2026",
        )

        c.save()

        pdf_url = url_for("static", filename=f"reports/{pdf_filename}", _external=True)
        return jsonify({"pdf_url": pdf_url})

    except Exception as e:
        print(f"PDF error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=False)