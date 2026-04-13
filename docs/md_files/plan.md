# PawPrint Project Refactor Plan

## Goal
- Separate frontend and backend into distinct directories.
- Integrate Gemini API for enhanced dog breed insights.
- Clean up the UI by removing unnecessary placeholder links.
- Improve the overall user experience and code structure.

## 1. Directory Structure Refactor
- **`backend/`**: Contains Flask server, ML model, and data processing.
  - `dog_model/` (moved)
  - `dataset_split/` (moved)
  - `static/` (backend-specific: `uploads`, `reports`)
  - `labels.json` (moved)
  - `serve.py` (updated and moved)
  - `train.py` (moved)
  - `requirements.txt` (updated with `google-generativeai`)
- **`frontend/`**: Contains UI components.
  - `images/` (moved)
  - `static/breed_examples/` (moved)
  - `index.html` (cleaned and moved)
  - `script.js` (updated and moved)

## 2. Gemini API Integration
- Add `google-generativeai` to backend dependencies.
- Implement a new endpoint or update the classification endpoint in `serve.py` to use Gemini for:
  - Detailed breed history.
  - Temperament and care tips.
  - Fun facts.
- Securely handle the API key (use environment variables).

## 3. UI/UX Improvements
- **Remove Placeholder Links**:
  - `Learn More`, `Pretrained Classifiers`, `Customers`
  - `Get Started`, `Contact us`, `Developers`, `API Docs`, `API Status`
  - `About`, `Blog`, `Support`
- **Refine Prompting**:
  - Improve the AI prompt to get high-quality, structured data about the breeds.
- **Enhanced Visuals**:
  - Ensure paths are correctly updated for images and examples.

## 4. Implementation Steps
1. Create `backend/` and `frontend/` folders.
2. Move files and update all internal paths (Flask static folders, script.js fetch URLs).
3. Clean up `index.html` footer and navigation.
4. Integrate Gemini API in `serve.py`.
5. Update `script.js` to handle the new Gemini-enhanced data.
6. Verify everything works seamlessly.
