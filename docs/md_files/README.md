# PawPrint - AI Dog Breed Classifier

PawPrint is an advanced dog breed classification application that uses Deep Learning (TensorFlow) for visual recognition and Gemini AI for detailed breed insights.

## Project Structure
- **`/frontend`**: Modern, responsive UI built with Tailwind CSS and Vite.
- **`/backend`**: Flask-based API serving predictions and integrating Gemini AI.

## Setup Instructions

### Backend Setup
1. Navigate to `/backend`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Create a `.env` file and add your `GEMINI_API_KEY`.
4. Run the server: `python serve.py`.

### Frontend Setup
1. Navigate to `/frontend`.
2. Install dependencies: `npm install`.
3. Start the development server: `npm run dev`.
4. Open the provided local URL (usually `http://localhost:5173`) in your browser.

## Features
- **Instant Breed Recognition**: High-accuracy classification using a custom TensorFlow model.
- **Gemini AI Insights**: Dynamic generation of breed history, traits, and fun facts.
- **Modern UI**: Fast and responsive interface using Vite and Tailwind CSS.
- **Printable Reports**: Save your results as a PDF or print them directly from the browser.
