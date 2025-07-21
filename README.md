# Extractor API

Extractor API is a FastAPI-based microservice that allows users to upload files (PDF, DOCX, or TXT), extract text, extract keywords using NLP, and classify the intent of the text.

## Features

- Accepts file uploads: PDF, DOCX, TXT
- Extracts text content
- Identifies top keywords using spaCy
- Classifies intent using rule-based logic
- Built with FastAPI for speed and flexibility

## Stack

- Python 3.11+
- FastAPI
- spaCy (`en_core_web_sm`)
- PyMuPDF (`fitz`)
- python-docx

## Folder Structure

extractor_api/
├── main.py
├── utils/
│   ├── file_reader.py
│   ├── extractor.py
│   └── intent.py
└── temp/ (auto-created for uploaded files)

## How to Run Locally

1. Install dependencies:

    pip install -r requirements.txt
    python -m spacy download en_core_web_sm

2. Start the API:

    uvicorn main:app --reload

3. Open docs:

    http://localhost:8000/docs

## Endpoint

POST /extract/

- Upload file (.pdf, .docx, .txt)
- Returns:
  - Extracted keywords
  - Classified intent

## License

This project is licensed under the MIT License.
