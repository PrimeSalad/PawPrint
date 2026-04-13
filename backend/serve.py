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
import google.generativeai as genai

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# -----------------------------
# FLASK APP & CONFIG
# -----------------------------
load_dotenv()
PORT = int(os.getenv("PORT", 5000))
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

app = Flask(__name__, static_folder="static")

@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

CORS(app)

# Configure Gemini
model_gemini = None
if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model_gemini = genai.GenerativeModel("gemini-1.5-flash")
        print("Gemini AI configured for descriptions.")
    except Exception as e:
        print(f"Gemini configuration failed: {e}")

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
    """Get rich info from Gemini or fallback to hardcoded data."""
    if model_gemini:
        prompt = f"Provide information about the dog breed '{breed.replace('_', ' ')}'. " \
                 "Return ONLY JSON with these keys: " \
                 '{"short_desc": "...", "traits": ["trait1", "trait2", "trait3"], "fun_fact": "..."}'
        try:
            response = model_gemini.generate_content(prompt)
            # Remove markdown code blocks if present
            clean_text = response.text.strip().replace("```json", "").replace("```", "")
            return json.loads(clean_text)
        except Exception as e:
            print(f"Gemini description failed: {e}")
    
    # Fallback data
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
        "engine": "TFLite CPU + Gemini API",
        "model_loaded": interpreter is not None,
        "gemini_active": model_gemini is not None
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

        # Get description (Gemini or Fallback)
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
