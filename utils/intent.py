import re

def classify_intent(text: str) -> str:
    """
    Basic rule-based intent classifier using keyword patterns.
    Returns intent label based on matched keywords.
    """

    # Normalize text to lowercase for case-insensitive matching
    text = text.lower()

    # Intent matching using regex keywords
    if re.search(r"\b(book|reserve|schedule|appointment)\b", text):
        return "Booking"

    elif re.search(r"\b(cancel|remove|unsubscribe|delete)\b", text):
        return "Cancellation"

    elif re.search(r"\b(info|information|details|learn|tell me about)\b", text):
        return "Information Request"

    elif re.search(r"\b(help|support|assist|issue|problem)\b", text):
        return "Support Request"

    elif re.search(r"\b(order|buy|purchase|payment)\b", text):
        return "Order Related"

    # Fallback if no pattern matches
    else:
        return "Unknown"
