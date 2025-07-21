import fitz  # PyMuPDF – used for reading PDF files
import docx  # python-docx – used for reading Word documents
import os

def extract_text_from_file(file_path: str) -> str:
    """
    Extract text from a supported file type (PDF, DOCX, or TXT).
    Returns the full extracted text as a string.
    """
    # Get the file extension in lowercase
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    extracted_text = ""

    # -------------------- PDF Reader --------------------
    if ext == ".pdf":
        try:
            pdf_doc = fitz.open(file_path)
            for page in pdf_doc:
                extracted_text += page.get_text()
            pdf_doc.close()
        except Exception as e:
            raise ValueError(f"Failed to read PDF: {e}")

    # -------------------- DOCX Reader --------------------
    elif ext == ".docx":
        try:
            docx_doc = docx.Document(file_path)
            for para in docx_doc.paragraphs:
                extracted_text += para.text + "\n"
        except Exception as e:
            raise ValueError(f"Failed to read DOCX: {e}")

    # -------------------- TXT Reader --------------------
    elif ext == ".txt":
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                extracted_text = file.read()
        except Exception as e:
            raise ValueError(f"Failed to read TXT: {e}")

    # -------------------- Unsupported Format --------------------
    else:
        raise ValueError(f"Unsupported file format: {ext}")

    # Clean up and return
    return extracted_text.strip()
