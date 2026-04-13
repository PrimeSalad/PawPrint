import os
import json
import uuid
import gc
from datetime import datetime

# CRITICAL FOR RENDER FREE TIER (512MB RAM):
# Disable GPU, limit threading, and minimize memory footprint
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from flask import Flask, request, jsonify, url_for, make_response
from flask_cors import CORS
from dotenv import load_dotenv
from PIL import Image
import numpy as np
import tensorflow as tf

# Force single-thread to prevent OOM/Timeout
tf.config.threading.set_inter_op_parallelism_threads(1)
tf.config.threading.set_intra_op_parallelism_threads(1)

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# -----------------------------
# FLASK APP & CORS
# -----------------------------
load_dotenv()
PORT = int(os.getenv("PORT", 5000))

app = Flask(__name__, static_folder="static")

@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        res = make_response()
        res.headers["Access-Control-Allow-Origin"] = "*"
        res.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        res.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return res

@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

CORS(app)


# -----------------------------
# LOAD TENSORFLOW MODEL
# -----------------------------
IMG_SIZE = 224
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "dog_model")
LABELS_PATH = os.path.join(BASE_DIR, "labels.json")

model = None
infer = None
idx_to_class = {}

print("Loading TensorFlow CPU model...")
try:
    # Load model with minimal memory footprint
    model = tf.saved_model.load(MODEL_PATH)
    infer = model.signatures["serving_default"]
    print("Model loaded successfully.")
    
    with open(LABELS_PATH, "r", encoding="utf-8") as f:
        class_indices = json.load(f)
    idx_to_class = {v: k for k, v in class_indices.items()}
    print(f"Loaded {len(idx_to_class)} labels.")
    
    # Run a dummy prediction to warm up the model and allocate memory
    dummy_input = tf.zeros([1, IMG_SIZE, IMG_SIZE, 3], dtype=tf.float32)
    infer(dummy_input)
    print("Model warmed up.")
except Exception as e:
    print(f"CRITICAL: Failed to load model or labels: {e}")


# -----------------------------
# HELPERS
# -----------------------------
def preprocess_image(image_stream):
    """Resize and normalize the image for TensorFlow."""
    img = Image.open(image_stream).convert("RGB")
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img_array = np.array(img).astype(np.float32) / 255.0
    return np.expand_dims(img_array, axis=0)


def get_hardcoded_info(breed):
    """Fallback data since Gemini is removed."""
    # Basic default dictionary
    return {
        "short_desc": f"The {breed.replace('_', ' ')} is a recognized canine breed known for its distinct features.",
        "traits": ["Loyal", "Energetic", "Companion"],
        "fun_fact": f"This breed has unique physical and behavioral traits."
    }


# -----------------------------
# ROUTES
# -----------------------------
@app.route("/")
def index():
    return jsonify({
        "status": "online", 
        "engine": "Local TensorFlow CPU",
        "model_loaded": infer is not None
    })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if infer is None:
            return jsonify({"error": "TensorFlow Model not loaded on server."}), 500

        if "image" not in request.files:
            return jsonify({"error": "No image provided"}), 400

        file = request.files["image"]
        if file.filename == "":
            return jsonify({"error": "Empty file uploaded"}), 400

        # Preprocess and predict
        x = preprocess_image(file.stream)
        preds_dict = infer(tf.constant(x))
        preds = list(preds_dict.values())[0].numpy()[0]

        # Get top prediction
        top_idx = int(preds.argsort()[-1])
        breed = idx_to_class.get(top_idx, "Unknown Breed")
        confidence = float(preds[top_idx])

        # Prepare response
        description = get_hardcoded_info(breed)
        results = [{
            "breed": breed,
            "confidence": confidence,
            "description": description,
            "temp_file_name": file.filename
        }]

        # CRITICAL: Force garbage collection to free RAM immediately
        del x, preds_dict, preds
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
        breed = data.get("breed", "Unknown Dog").replace('_', ' ')
        
        pdf_filename = f"report_{uuid.uuid4().hex[:8]}.pdf"
        reports_dir = os.path.join(app.static_folder, "reports")
        os.makedirs(reports_dir, exist_ok=True)
        pdf_path = os.path.join(reports_dir, pdf_filename)

        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.setFont("Helvetica-Bold", 20)
        c.drawString(100, 700, f"BREED REPORT: {breed.upper()}")
        c.setFont("Helvetica", 12)
        c.drawString(100, 670, f"The {breed} is a recognized canine breed known for its distinct features.")
        c.save()

        pdf_url = url_for("static", filename=f"reports/{pdf_filename}", _external=True)
        return jsonify({"pdf_url": pdf_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
