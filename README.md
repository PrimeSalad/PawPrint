# PawPrint - AI Dog Breed Classifier ✨

PawPrint is a premium dog breed classification application that uses Deep Learning (TensorFlow Lite) for high-accuracy visual recognition and a comprehensive local database for detailed breed insights.

## Features
- **Instant Breed Recognition**: High-accuracy classification using a custom TensorFlow Lite model supporting 122 dog breeds.
- **GOD MODE Premium UI**: Professional, high-fidelity user interface with biometric scanning animations and real-time visual feedback.
- **Comprehensive Local Database**: Detailed insights for 122 breeds, including history, traits, fun facts, origin, size, temperament, and health notes.
- **Internet-Ready Photos**: Reliable, high-quality breed images sourced from Wikimedia Commons.
- **Professional PDF Reports**: Generate and download detailed analytical reports for any detected breed.
- **Zero-Latency Insights**: No external AI API dependencies, ensuring lightning-fast results and 100% privacy.

## Project Structure
- **`/frontend`**: Premium UI built with Tailwind CSS, featuring advanced scanning animations and high-fidelity layout.
- **`/backend`**: Flask-based API serving predictions using TFLite and a 122-breed comprehensive local database.

## Setup Instructions

### Backend Setup
1. Navigate to `/backend`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the server: `python serve.py`.

### Frontend Setup
1. Open `frontend/index.html` in your browser (no build step required for static serving).
2. Ensure the backend is running for prediction functionality.

## Technical Details
- **ML Model**: TensorFlow Lite (.tflite) for optimized on-device or server-side inference.
- **Data Source**: Custom-built `breed_database.py` containing curated data for all supported labels.
- **Animations**: CSS-driven biometric scanning effects and premium HUD visualizations.
- **PDF Generation**: Powered by ReportLab for professional-grade document creation.
