# PawPrint Deployment Guide

## Overview
- **Frontend**: Deployed on Vercel
- **Backend**: Deployed on Render
- **Model**: TFLite (2.54 MB), tracked with Git LFS
- **Breed DB**: Local database (no external APIs)

## Prerequisites
- Render account
- Vercel account
- Git LFS installed locally (`git lfs install`)

## Step 1: Initialize Git LFS (First Time Only)

```bash
git lfs install
git add .gitattributes
git commit -m "Add Git LFS configuration"
git push
```

## Step 2: Deploy Backend to Render

### Option A: Automatic (Recommended)
1. Go to [render.com](https://render.com)
2. Sign in with GitHub
3. Click "New +" → "Web Service"
4. Select your PawPrint repository
5. Render will auto-detect `backend/render.yaml` and use its configuration

### Option B: Manual Configuration
If automatic detection doesn't work:
1. Create a Web Service manually
2. Set the following:
   - **Name**: pawprint-backend
   - **Environment**: Python 3.11
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT serve:app --timeout 120 --workers 2`
   - **Root Directory**: `backend`

### Step 3: NO Environment Variables Needed
The backend now uses a local breed database. No `GEMINI_API_KEY` is required!

### Step 4: Verify Backend is Running
Wait for deployment to complete, then test:
```bash
curl https://your-pawprint-backend.onrender.com/
```

Expected response:
```json
{
  "status": "online",
  "engine": "TFLite CPU + Local Breed DB",
  "model_loaded": true,
  "version": "2.0"
}
```

## Step 5: Update Frontend Render URL (If Different)

If your Render URL is different from `https://pawprint-backend.onrender.com`, update it in:

**File**: `frontend/vercel.json`
```json
{
  "rewrites": [
    { "source": "/api/:path*", "destination": "https://YOUR-RENDER-URL.onrender.com/:path*" }
  ]
}
```

## Step 6: Deploy Frontend to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click "Add New" → "Project"
3. Select your PawPrint repository
4. Set Root Directory: `frontend`
5. Deploy!

## Step 7: Verify End-to-End

1. Go to your Vercel domain (e.g., `https://pawprint.vercel.app`)
2. Upload a dog image
3. Verify the prediction works and shows the breed with local breed info

## Troubleshooting

### "TFLite Model not loaded on server"
- Check Render logs: Your service → Logs
- Look for "CRITICAL" messages during startup
- Ensure `dog_model.tflite` file is present (check Git LFS status)
- Verify `requirements.txt` includes `tflite-runtime` or `tensorflow`

### Model Takes Too Long to Load
- Render free tier has limited resources
- Consider upgrading to Render's paid tier
- Model is 2.54 MB and should load within 30 seconds

### CORS Errors
- Frontend proxy (`/api`) should handle CORS automatically
- Backend Flask app has CORS enabled via `flask-cors`
- Check Vercel function logs for proxy errors

### Git LFS Issues
```bash
# Check LFS status
git lfs ls-files

# Reinstall LFS
git lfs install --force

# Migrate file to LFS
git lfs migrate import --include="*.tflite"
git push -u origin main
```

## File Structure

```
PawPrint/
├── backend/
│   ├── render.yaml          ← Render deployment config
│   ├── requirements.txt      ← Python dependencies (no Gemini!)
│   ├── serve.py            ← Flask application with local breed DB
│   ├── dog_model.tflite     ← ML Model (2.54 MB)
│   └── labels.json         ← Class labels
├── frontend/
│   ├── vercel.json         ← Vercel config with Render proxy
│   ├── script.js           ← Main app logic
│   └── package.json        ← Frontend dependencies
└── .gitattributes          ← Git LFS configuration
```

## Performance Notes

- **Model Loading**: ~5-10 seconds on Render free tier
- **Prediction**: ~2-3 seconds per image
- **Memory**: TFLite runtime optimized for low-memory environments
- **Breed Info**: Loaded locally, no API latency

## Support

For issues:
1. Check Render logs for backend errors
2. Check Vercel Function logs for proxy errors
3. Check browser console for frontend errors
4. Verify backend is running with: `curl https://your-backend/`
