import spacy

# Load the English NLP model (make sure it's installed beforehand)
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text: str, max_keywords: int = 10) -> list:
    """
    Extracts keywords from input text using spaCy.
    Combines noun chunks and named entities for broader coverage.
    """

    doc = nlp(text)
    keywords = set()

    # 🔹 Add all noun chunks (e.g., "machine learning", "user experience")
    for chunk in doc.noun_chunks:
        if len(chunk.text.strip()) > 2:
            keywords.add(chunk.text.strip().lower())

    # 🔹 Add named entities (e.g., "India", "Google")
    for ent in doc.ents:
        if len(ent.text.strip()) > 2:
            keywords.add(ent.text.strip().lower())

    # 🔸 Return top N keywords as a list
    return list(keywords)[:max_keywords]
