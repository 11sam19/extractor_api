from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os

from utils.file_reader import extract_text_from_file
from utils.extractor import extract_keywords
from utils.intent import classify_intent

app = FastAPI()

@app.get("/")
async def root():
    # Health check route
    return {"message": "Extractor API is running 🚀"}

@app.post("/extract/")
async def extract_from_file(file: UploadFile = File(...)):
    try:
        # Ensure 'temp' folder exists for saving uploads
        os.makedirs("temp", exist_ok=True)

        # Save the uploaded file temporarily
        file_location = os.path.join("temp", file.filename)
        with open(file_location, "wb") as f:
            f.write(await file.read())

        # Step 1: Extract raw text from the uploaded file
        text = extract_text_from_file(file_location)

        # Step 2: Identify key phrases from text
        keywords = extract_keywords(text)

        # Step 3: Detect user intent based on content
        intent = classify_intent(text)

        # Step 4: Clean up temporary file
        os.remove(file_location)

        # Step 5: Return structured response
        return JSONResponse(content={
            "filename": file.filename,
            "keywords": keywords,
            "intent": intent
        })

    except Exception as e:
        # Error response for failed operations
        return JSONResponse(status_code=500, content={"error": str(e)})
