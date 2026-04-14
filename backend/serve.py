import os
import json
import uuid
import gc
import numpy as np
from datetime import datetime
from PIL import Image

# Use tflite_runtime if possible to save memory, fallback to full tensorflow
tflite = None
try:
    import tflite_runtime.interpreter as tflite_interp
    tflite = tflite_interp
    print("[OK] Using tflite_runtime (optimized).")
except ImportError:
    try:
        import tensorflow.lite as tflite_tf
        tflite = tflite_tf
        print("[OK] Using tensorflow.lite (full TensorFlow).")
    except ImportError:
        import tensorflow as tf
        tflite = tf.lite
        print("[OK] Using tensorflow.lite (from full TensorFlow).")
        
if tflite is None:
    raise ImportError("TFLite interpreter not available. Please install tensorflow or tflite-runtime.")

from flask import Flask, request, jsonify, url_for, make_response
from flask_cors import CORS
from dotenv import load_dotenv
from breed_database import BREED_DATABASE

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# -----------------------------
# FLASK APP & CONFIG
# -----------------------------
# ✂ REMOVED: import google.generativeai as genai (Line 31)
# ✂ REMOVED: GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") (Line 42)
load_dotenv()
PORT = int(os.getenv("PORT", 5000))

app = Flask(__name__, static_folder="static")

@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

CORS(app)

# Breed information database (replaces Gemini)
BREED_INFO = {
    "dachshund": {
        "short_desc": "The Dachshund is a small hound breed known for its distinctive elongated body and short legs. Originally bred to hunt badgers, they are energetic, intelligent, and loyal companions.",
        "traits": ["Clever", "Courageous", "Friendly", "Curious"],
        "fun_fact": "Their name means 'badger dog' in German, reflecting their original hunting purpose.",
        "origin": "Germany, 15th century",
        "size": "8-9 inches, 16-32 lbs",
        "temperament": "Independent, playful, stubborn but affectionate",
        "health_notes": "Prone to back issues due to long spine; needs exercise and back support",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Dachshund_Longhaired_001.jpg/1024px-Dachshund_Longhaired_001.jpg"
    },
    "chihuahua": {
        "short_desc": "The Chihuahua is the smallest dog breed, known for its tiny size but big personality. Despite their delicate appearance, they are spirited and confident companions.",
        "traits": ["Sassy", "Loyal", "Energetic", "Alert"],
        "fun_fact": "Chihuahuas can have soft or smooth coats and are famous for their trembling when cold or excited.",
        "origin": "Mexico, ancient Aztec times",
        "size": "5-8 inches, 2-6 lbs",
        "temperament": "Confident, alert, protective despite small size",
        "health_notes": "Sensitive to cold; prone to dental issues; needs protection from larger dogs",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Chihuahua1.jpg/1024px-Chihuahua1.jpg"
    },
    "siberian_husky": {
        "short_desc": "The Siberian Husky is a large, energetic sled dog breed known for its striking appearance with ice-blue eyes and thick double coat. They are pack-oriented and require plenty of exercise.",
        "traits": ["Energetic", "Friendly", "Independent", "Pack-Oriented"],
        "fun_fact": "Huskies have a double coat that sheds heavily twice a year, requiring regular grooming.",
        "origin": "Siberia, Russia - bred by Chukchi people",
        "size": "20-24 inches, 35-60 lbs",
        "temperament": "Friendly, outgoing, mischievous, escape artists",
        "health_notes": "High energy requirements; prone to hip dysplasia; must have secure fencing",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Siberian_Husky_blue_eyes_Flickr.jpg/1024px-Siberian_Husky_blue_eyes_Flickr.jpg"
    },
    "golden_retriever": {
        "short_desc": "The Golden Retriever is a large, friendly dog breed known for their intelligence and gentle temperament. They are excellent family pets and are highly trainable.",
        "traits": ["Intelligent", "Friendly", "Devoted", "Outgoing"],
        "fun_fact": "Golden Retrievers were originally bred in Scotland to retrieve game birds during hunting.",
        "origin": "Scotland, 19th century",
        "size": "20-24 inches, 55-75 lbs",
        "temperament": "Friendly, tolerant, devoted, excellent with families",
        "health_notes": "Prone to hip dysplasia, heart disease, and cancer; needs regular exercise",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Camponotus_flavomarginatus_ant.jpg/1024px-Golden_Retriever.jpg"
    },
    "labrador_retriever": {
        "short_desc": "The Labrador Retriever is a large, athletic dog breed known for their friendly nature and exceptional training ability. They excel as service and therapy dogs.",
        "traits": ["Outgoing", "Even-Tempered", "Intelligent", "Loyal"],
        "fun_fact": "Labs come in three colors: black, yellow, and chocolate, each equally recognized and valued.",
        "origin": "Canada (Newfoundland), 19th century",
        "size": "21-24 inches, 55-80 lbs",
        "temperament": "Outgoing, even-tempered, highly trainable, great retrievers",
        "health_notes": "Prone to hip dysplasia and obesity; needs regular exercise and proper diet",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Labrador_on_Quantock_%282175262184%29.jpg/1024px-Labrador_on_Quantock_%282175262184%29.jpg"
    },
    "german_shepherd": {
        "short_desc": "The German Shepherd is a large, intelligent working dog breed known for their versatility and loyalty. They excel in police, military, and search-and-rescue roles.",
        "traits": ["Confident", "Intelligent", "Loyal", "Alert"],
        "fun_fact": "German Shepherds are one of the most versatile working dogs, used in military and police worldwide.",
        "origin": "Germany, 1899",
        "size": "22-26 inches, 50-90 lbs",
        "temperament": "Confident, courageous, extremely versatile, loyal protectors",
        "health_notes": "Prone to hip/elbow dysplasia, degenerative myelopathy; needs mental stimulation",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/German_Shepherd_-_DSC_4797.JPG/1024px-German_Shepherd_-_DSC_4797.JPG"
    },
    "bulldog": {
        "short_desc": "The Bulldog is a medium-sized breed known for their stocky build, wrinkled face, and gentle disposition. Despite their intimidating appearance, they are affectionate and loyal.",
        "traits": ["Gentle", "Courageous", "Affectionate", "Stubborn"],
        "fun_fact": "Bulldogs were originally bred for the cruel sport of bull-baiting in medieval England.",
        "origin": "England, 13th century",
        "size": "14-15 inches, 40-50 lbs",
        "temperament": "Gentle, affectionate, dignified, determined",
        "health_notes": "Brachycephalic breed with breathing issues; prone to skin fold infections; heat sensitive",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/English_Bulldog_ad1.jpg/1024px-English_Bulldog_ad1.jpg"
    },
    "poodle": {
        "short_desc": "The Poodle is an intelligent, athletic dog breed available in three sizes (Standard, Miniature, Toy). They are known for their curly coat and exceptional trainability.",
        "traits": ["Intelligent", "Active", "Elegant", "Obedient"],
        "fun_fact": "Poodles have a hypoallergenic coat that sheds minimally, making them great for allergy sufferers.",
        "origin": "Germany/France, 17th century",
        "size": "Standard: 22+ inches; Miniature: 11-15 inches",
        "temperament": "Intelligent, active, elegant, eager to please",
        "health_notes": "Prone to hip dysplasia and ear infections; requires regular grooming and mental stimulation",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Apricot_Standard_Poodle.jpg/1024px-Apricot_Standard_Poodle.jpg"
    },
    "french_bulldog": {
        "short_desc": "The French Bulldog is a small, muscular dog breed with distinctive bat-like ears. They are playful, affectionate, and adapt well to various living situations.",
        "traits": ["Playful", "Affectionate", "Adaptable", "Alert"],
        "fun_fact": "Despite the name, French Bulldogs were actually developed in England as a smaller version of English Bulldogs.",
        "origin": "France, 1860s (derived from English Bulldog)",
        "size": "11-13 inches, 28 lbs",
        "temperament": "Playful, affectionate, adaptable, minimal exercise needs",
        "health_notes": "Brachycephalic breed; prone to breathing problems, overheating, spine issues",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Frenchie_Isabella.JPG/1024px-Frenchie_Isabella.JPG"
    },
    "beagle": {
        "short_desc": "The Beagle is a small scent hound breed known for their keen sense of smell and curious nature. They are pack dogs that enjoy family life and outdoor adventures.",
        "traits": ["Curious", "Friendly", "Determined", "Merry"],
        "fun_fact": "Beagles have approximately 220 million scent receptors, making them excellent at tracking.",
        "origin": "England, medieval times",
        "size": "13-15 inches, 24-30 lbs",
        "temperament": "Merry, curious, determined, friendly pack hunters",
        "health_notes": "Prone to ear infections, obesity, epilepsy; excellent noses make them escape artists",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Beagle_4.jpg/1024px-Beagle_4.jpg"
    },
    "rottweiler": {
        "short_desc": "The Rottweiler is a large, powerful dog breed known for their confident nature and protective instincts. When properly trained and socialized, they are loyal and loving companions.",
        "traits": ["Confident", "Loyal", "Protective", "Intelligent"],
        "fun_fact": "Rottweilers were originally used as herding dogs and later as cart-pulling dogs in Roman times.",
        "origin": "Germany (Rottweil region), medieval times",
        "size": "22-27 inches, 80-135 lbs",
        "temperament": "Confident, courageous, good-natured, self-assured, loyal",
        "health_notes": "Prone to hip dysplasia, heart problems; needs firm, early socialization and training",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Rottweiler_standing.jpg/1024px-Rottweiler_standing.jpg"
    },
    "yorkshire_terrier": {
        "short_desc": "The Yorkshire Terrier is a small terrier breed with long, silky coat and a big personality. They are confident, spirited companions that enjoy attention and playtime.",
        "traits": ["Confident", "Spirited", "Affectionate", "Playful"],
        "fun_fact": "Despite their delicate appearance, Yorkshire Terriers were originally bred to catch rats in mills.",
        "origin": "England (Yorkshire region), 19th century",
        "size": "7-8 inches, 4-7 lbs",
        "temperament": "Spirited, confident, affectionate, playful hunters",
        "health_notes": "Prone to patellar luxation, dental issues, eye problems; needs regular grooming",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Yorkshireterrier_Groom.jpg/1024px-Yorkshireterrier_Groom.jpg"
    }
}

print("[OK] Breed information database loaded (Gemini removed).")

# -----------------------------
# LOAD TFLITE MODEL
# -----------------------------
IMG_SIZE = 224
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TFLITE_MODEL_PATH = os.path.join(BASE_DIR, "dog_model.tflite")
LABELS_PATH = os.path.join(BASE_DIR, "labels.json")

interpreter = None
input_details = None
output_details = None
idx_to_class = {}

print(f"Loading TFLite model from {TFLITE_MODEL_PATH}...")
try:
    if os.path.exists(TFLITE_MODEL_PATH):
        print(f"  [INFO] Model file found ({os.path.getsize(TFLITE_MODEL_PATH) / 1024 / 1024:.2f} MB)")
        try:
            interpreter = tflite.Interpreter(model_path=TFLITE_MODEL_PATH)
            interpreter.allocate_tensors()
            
            input_details = interpreter.get_input_details()
            output_details = interpreter.get_output_details()
            print("[OK] TFLite Model loaded successfully.")
            
            with open(LABELS_PATH, "r", encoding="utf-8") as f:
                class_indices = json.load(f)
            idx_to_class = {v: k for k, v in class_indices.items()}
            print(f"[OK] Loaded {len(idx_to_class)} labels.")
        except Exception as e:
            print(f"[ERROR] Model loading failed: {type(e).__name__}: {str(e)}")
            print(f"[INFO] Attempting workaround: reloading interpreter...")
            try:
                # Try reloading with different settings
                interpreter = None
                import gc
                gc.collect()
                interpreter = tflite.Interpreter(model_path=TFLITE_MODEL_PATH)
                interpreter.allocate_tensors()
                input_details = interpreter.get_input_details()
                output_details = interpreter.get_output_details()
                print("[OK] Model loaded with workaround.")
                with open(LABELS_PATH, "r", encoding="utf-8") as f:
                    class_indices = json.load(f)
                idx_to_class = {v: k for k, v in class_indices.items()}
                print(f"[OK] Loaded {len(idx_to_class)} labels.")
            except Exception as e2:
                print(f"[CRITICAL] TFLite model still failed: {str(e2)}")
                print(f"[INFO] Using TensorFlow directly may help on Render.")
    else:
        print(f"[CRITICAL] TFLite model not found at {TFLITE_MODEL_PATH}")
except Exception as e:
    print(f"[CRITICAL] Unexpected error during model setup: {e}")


# -----------------------------
# HELPERS
# -----------------------------
def preprocess_image(image_stream):
    """Resize and normalize the image for TFLite."""
    img = Image.open(image_stream).convert("RGB")
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img_array = np.array(img).astype(np.float32) / 255.0
    return np.expand_dims(img_array, axis=0)


def get_breed_info(breed):
    """Get breed information from comprehensive local database (all 122 breeds)."""
    breed_key = breed.lower()
    if breed_key in BREED_DATABASE:
        return BREED_DATABASE[breed_key]
    
    # Fallback for unknown breeds
    return {
        "short_desc": f"The {breed.replace('_', ' ')} is a recognized canine breed known for its distinct features.",
        "traits": ["Loyal", "Energetic", "Companion"],
        "fun_fact": f"This breed has unique physical and behavioral traits.",
        "origin": "Unknown",
        "size": "Variable",
        "temperament": "Varies by individual dog",
        "health_notes": "Consult a veterinarian for breed-specific health information",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Beagle_4.jpg/1024px-Beagle_4.jpg"
    }


# -----------------------------
# ROUTES
# -----------------------------
@app.route("/")
def index():
    return jsonify({
        "status": "online", 
        "engine": "TFLite CPU + Local Breed DB",
        "model_loaded": interpreter is not None,
        "version": "2.0"
    })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if interpreter is None:
            return jsonify({"error": "TFLite Model not loaded on server."}), 500

        if "image" not in request.files:
            return jsonify({"error": "No image provided"}), 400

        file = request.files["image"]
        if file.filename == "":
            return jsonify({"error": "Empty file uploaded"}), 400

        # Preprocess
        x = preprocess_image(file.stream)
        
        # Run TFLite inference
        interpreter.set_tensor(input_details[0]['index'], x)
        interpreter.invoke()
        preds = interpreter.get_tensor(output_details[0]['index'])[0]

        # Get top prediction
        top_idx = int(preds.argsort()[-1])
        breed = idx_to_class.get(top_idx, "Unknown Breed")
        confidence = float(preds[top_idx])

        # Get description from local breed database
        description = get_breed_info(breed)
        
        results = [{
            "breed": breed,
            "confidence": confidence,
            "description": description,
            "temp_file_name": file.filename
        }]

        # CRITICAL: Force garbage collection
        del x, preds
        gc.collect()

        return jsonify({"predictions": results})

    except Exception as e:
        print(f"Prediction Error: {e}")
        gc.collect()
        return jsonify({"error": f"Server crash during prediction: {str(e)}"}), 500

@app.route("/generate_pdf", methods=["POST"])
def generate_pdf():
    try:
        data = request.get_json(silent=True) or {}
        breed = data.get("breed", "Unknown Dog").replace('_', ' ').title()
        breed_key = breed.lower().replace(' ', '_')
        
        pdf_filename = f"report_{uuid.uuid4().hex[:8]}.pdf"
        reports_dir = os.path.join(app.static_folder, "reports")
        os.makedirs(reports_dir, exist_ok=True)
        pdf_path = os.path.join(reports_dir, pdf_filename)

        # Get breed info
        breed_info = get_breed_info(breed_key)
        
        # Create PDF
        c = canvas.Canvas(pdf_path, pagesize=letter)
        width, height = letter
        
        # Set colors
        primary_color = "#e26215"  # PawPrint orange
        dark_color = "#7a3f1a"     # Dark brown
        light_bg = "#fef9f6"       # Light background
        
        # Helper to convert hex to RGB
        def hex_to_rgb(hex_color):
            h = hex_color.lstrip('#')
            return tuple(int(h[i:i+2], 16)/255.0 for i in (0, 2, 4))
        
        from reportlab.lib.colors import HexColor
        primary = HexColor(primary_color)
        dark = HexColor(dark_color)
        
        # Top banner
        c.setFillColor(primary)
        c.rect(0, height - 100, width, 100, fill=True, stroke=False)
        
        # Title
        c.setFillColor(colors.whitesmoke)
        c.setFont("Helvetica-Bold", 32)
        c.drawString(50, height - 55, "BREED REPORT")
        
        c.setFont("Helvetica", 14)
        c.drawString(50, height - 75, f"Identified Breed: {breed}")
        
        # Main content area
        y = height - 130
        margin = 50
        
        # Breed title
        c.setFillColor(dark)
        c.setFont("Helvetica-Bold", 24)
        c.drawString(margin, y, breed)
        y -= 35
        
        # Short description
        c.setFillColor(colors.black)
        c.setFont("Helvetica", 11)
        desc = breed_info.get("short_desc", "")
        for line in _wrap_text(desc, 90):
            c.drawString(margin, y, line)
            y -= 14
        y -= 10
        
        # Two-column layout for details
        col_width = (width - 2*margin) / 2
        col1_x = margin
        col2_x = margin + col_width + 20
        
        def draw_section(x, y, title, content):
            c.setFillColor(primary)
            c.setFont("Helvetica-Bold", 12)
            c.drawString(x, y, title)
            y -= 16
            c.setFillColor(colors.black)
            c.setFont("Helvetica", 10)
            for line in _wrap_text(content, 35):
                c.drawString(x, y, line)
                y -= 12
            return y
        
        y_left = y
        y_right = y
        
        # Origin
        origin = breed_info.get("origin", "Unknown")
        y_left = draw_section(col1_x, y_left, "ORIGIN:", origin)
        y_left -= 8
        
        # Size
        size = breed_info.get("size", "Unknown")
        y_left = draw_section(col1_x, y_left, "SIZE:", size)
        y_left -= 8
        
        # Temperament
        temp = breed_info.get("temperament", "Unknown")
        y_right = draw_section(col2_x, y_right, "TEMPERAMENT:", temp)
        y_right -= 8
        
        # Health Notes
        health = breed_info.get("health_notes", "Consult a veterinarian")
        y_right = draw_section(col2_x, y_right, "HEALTH NOTES:", health)
        
        # Use minimum of both columns
        y = min(y_left, y_right) - 15
        
        # Traits
        c.setFillColor(primary)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(margin, y, "KEY TRAITS:")
        y -= 16
        c.setFillColor(colors.black)
        c.setFont("Helvetica", 10)
        traits = breed_info.get("traits", [])
        traits_text = ", ".join(traits)
        for line in _wrap_text(traits_text, 90):
            c.drawString(margin, y, "• " + line)
            y -= 12
        y -= 10
        
        # Fun Fact
        c.setFillColor(primary)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(margin, y, "FUN FACT:")
        y -= 16
        c.setFillColor(dark)
        c.setFont("Helvetica-Oblique", 10)
        fun_fact = breed_info.get("fun_fact", "")
        for line in _wrap_text(fun_fact, 90):
            c.drawString(margin, y, line)
            y -= 12
        
        # Footer
        y = 30
        c.setFillColor(colors.grey)
        c.setFont("Helvetica", 9)
        c.drawString(margin, y, "PawPrint AI - Dog Breed Scanner")
        c.drawString(width - margin - 150, y, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        c.save()

        pdf_url = url_for("static", filename=f"reports/{pdf_filename}", _external=True)
        return jsonify({"pdf_url": pdf_url})
    except Exception as e:
        print(f"PDF Error: {e}")
        return jsonify({"error": str(e)}), 500


def _wrap_text(text, max_width_chars):
    """Wrap text to fit within character width."""
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        if len(' '.join(current_line + [word])) <= max_width_chars:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
