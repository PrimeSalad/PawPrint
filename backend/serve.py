# backend/serve.py
import os
import io
import json
from datetime import datetime
from flask import Flask, request, jsonify, url_for, send_from_directory
from flask_cors import CORS, cross_origin
import tensorflow as tf
from PIL import Image
import numpy as np
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY and GEMINI_API_KEY != "your_api_key_here":
    genai.configure(api_key=GEMINI_API_KEY)
    model_gemini = genai.GenerativeModel('gemini-2.5-flash')
else:
    model_gemini = None
    print("Warning: GEMINI_API_KEY not set. Using fallback descriptions.")

app = Flask(__name__, static_folder="static")
CORS(app, resources={r"/*": {"origins": "*"}})

# -----------------------------
# MODEL LOAD
# -----------------------------
IMG_SIZE = 224
MODEL_PATH = "dog_model"

print("Loading model...")
model = tf.saved_model.load(MODEL_PATH)
infer = model.signatures["serving_default"]
print("Model loaded.")

# -----------------------------
# LABELS
# -----------------------------
with open("labels.json", "r") as f:
    class_indices = json.load(f)
idx_to_class = {v: k for k, v in class_indices.items()}
print("Labels loaded.")

def preprocess_image(image_stream):
    img = Image.open(image_stream).convert('RGB')
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img_array = np.array(img).astype(np.float32) / 255.0
    return np.expand_dims(img_array, axis=0)

async def get_gemini_description(breed):
    if not model_gemini:
        return f"The {breed} is a unique and wonderful dog breed."
    
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
        # Attempt to parse JSON from response
        content = response.text
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        return json.loads(content)
    except Exception as e:
        print(f"Gemini error for {breed}: {e}")
        return {
            "short_desc": f"The {breed} is known for its distinctive features and loyal nature.",
            "traits": ["Loyal", "Energetic", "Intelligent"],
            "fun_fact": "This breed has a rich history as a companion dog."
        }

@app.route("/")
def index():
    return "PawPrint Backend API is running."

@app.route("/predict", methods=["POST"])
@cross_origin(origin="*")
def predict():
    try:
        if "image" not in request.files:
            return jsonify({"error": "no image file"}), 400

        file = request.files["image"]
        x = preprocess_image(file.stream)

        # Make prediction
        preds_dict = infer(tf.constant(x))
        preds = list(preds_dict.values())[0].numpy()[0]

        top_indices = preds.argsort()[-1:][::-1] # Just top 1 for now to simplify

        results = []
        for idx in top_indices:
            breed = idx_to_class[int(idx)]
            conf = float(preds[int(idx)])

            # Get Gemini description (sync wrapper for now or just run)
            # Since this is Flask, we'll do it synchronously
            description = get_gemini_info_sync(breed)

            results.append({
                "breed": breed,
                "confidence": conf,
                "description": description,
                "temp_file_name": file.filename
            })

        return jsonify({"predictions": results})

    except Exception as e:
        print("Predict error:", e)
        return jsonify({"error": str(e)}), 500

def get_gemini_info_sync(breed):
    return {
        "short_desc": f"The {breed} is a wonderful and unique breed known for its distinctive features.",
        "traits": ["Loyal", "Energetic", "Friendly"],
        "fun_fact": f"The {breed} has a rich history and makes a great companion."
    }

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import uuid
import textwrap
from datetime import datetime

@app.route("/generate_pdf", methods=["POST"])
@cross_origin(origin="*")
def generate_pdf():
    try:
        data = request.get_json()
        breed = data.get("breed", "Unknown Dog")
        
        report_text = f"Detailed report for {breed} is currently unavailable as Gemini is not configured."
        if model_gemini:
            prompt = f"Write a detailed, professional report about the dog breed: {breed}. Include its history, general temperament, and basic care instructions. Format it cleanly as plain text without markdown asterisks or hashes. Limit to 3 or 4 paragraphs."
            try:
                response = model_gemini.generate_content(prompt)
                report_text = response.text.replace('*', '').replace('#', '')
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
        
        # Generate PDF
        pdf_filename = f"{breed.replace(' ', '_')}_report_{uuid.uuid4().hex[:8]}.pdf"
        reports_dir = os.path.join(app.static_folder, "reports")
        os.makedirs(reports_dir, exist_ok=True)
        pdf_path = os.path.join(reports_dir, pdf_filename)
        
        c = canvas.Canvas(pdf_path, pagesize=letter)
        width, height = letter
        
        # Draw Background
        c.setFillColor(colors.HexColor('#faf8f6'))
        c.rect(0, 0, width, height, stroke=0, fill=1)
        
        # Top Accent Line
        c.setFillColor(colors.HexColor('#e26215'))
        c.rect(0, height - 15, width, 15, stroke=0, fill=1)
        
        # Add Logo
        base_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(base_dir, "..", "frontend", "images", "logo.png")
        if os.path.exists(logo_path):
            try:
                c.drawImage(logo_path, 40, height - 85, width=160, preserveAspectRatio=True, mask='auto')
            except Exception as img_err:
                print("Logo draw error:", img_err)
        
        # Header Text
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(colors.HexColor('#8a4f2a'))
        c.drawString(width - 240, height - 50, "AI BREED CLASSIFICATION")
        
        # Date
        c.setFont("Helvetica", 10)
        c.setFillColor(colors.HexColor('#a08a7b'))
        c.drawString(width - 240, height - 65, f"Generated: {datetime.now().strftime('%B %d, %Y')}")
        
        # Title Background Box
        c.setFillColor(colors.HexColor('#e26215'))
        c.roundRect(40, height - 160, width - 80, 50, 10, stroke=0, fill=1)
        
        # Title
        c.setFont("Helvetica-Bold", 20)
        c.setFillColor(colors.white)
        c.drawString(60, height - 143, f"BREED REPORT: {breed.upper()}")
        
        # Content Setup
        c.setFont("Helvetica", 12)
        c.setFillColor(colors.HexColor('#7a3f1a'))
        text_object = c.beginText(50, height - 200)
        text_object.setLeading(20) # Add comfortable line spacing
        
        # Handle newlines and wrap text carefully
        for paragraph in report_text.split('\n'):
            if not paragraph.strip():
                continue
                
            # If paragraph looks like a header (starts with bold or uppercase)
            if paragraph.isupper() or paragraph.startswith('**'):
                c.drawText(text_object)
                c.setFont("Helvetica-Bold", 14)
                c.setFillColor(colors.HexColor('#e26215'))
                text_object = c.beginText(50, text_object.getY() - 10)
                text_object.setLeading(20)
                paragraph = paragraph.replace('**', '')
                text_object.textLine(paragraph)
                c.drawText(text_object)
                c.setFont("Helvetica", 12)
                c.setFillColor(colors.HexColor('#7a3f1a'))
                text_object = c.beginText(50, text_object.getY() - 5)
                text_object.setLeading(20)
                continue

            lines = textwrap.wrap(paragraph.replace('**', ''), width=80)
            for line in lines:
                # Auto page break if too low
                if text_object.getY() < 100:
                    c.drawText(text_object)
                    c.showPage()
                    c.setFillColor(colors.HexColor('#faf8f6'))
                    c.rect(0, 0, width, height, stroke=0, fill=1)
                    c.setFont("Helvetica", 12)
                    c.setFillColor(colors.HexColor('#7a3f1a'))
                    text_object = c.beginText(50, height - 50)
                    text_object.setLeading(20)
                text_object.textLine(line)
                
            text_object.textLine("") # Extra space between paragraphs
                
        c.drawText(text_object)
        
        # Footer
        c.setFillColor(colors.HexColor('#1a0f08'))
        c.rect(0, 0, width, 60, stroke=0, fill=1)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(colors.HexColor('#e26215'))
        c.drawCentredString(width / 2.0, 35, "PAWPRINT AI")
        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor('#8a7563'))
        c.drawCentredString(width / 2.0, 20, "Identifying stories, one pawprint at a time. | © 2026")
        
        c.save()
        
        pdf_url = url_for('static', filename=f'reports/{pdf_filename}', _external=True)
        return jsonify({"pdf_url": pdf_url})
    except Exception as e:
        print("PDF error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
