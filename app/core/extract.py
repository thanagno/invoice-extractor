import re
from typing import Dict

def is_invoice(text: str) -> bool:
    """Check if the document is likely an invoice."""
    invoice_keywords = [
        "invoice", "facture", "amount", "total", "TVA", "balance",  # English/French keywords
        "rechnung", "betrag", "gesamt", "steuern", "saldo",  # German keywords
        "τιμολόγιο", "ποσό", "σύνολο", "φόρος", "υπόλοιπο"  # Greek keywords
    ]
    return any(keyword.lower() in text.lower() for keyword in invoice_keywords)

def extract_invoice_details(text: str) -> Dict[str, str]:
    """Extract details from the invoice text."""
    details = {}

    # Common patterns across languages
    details['Invoice Number'] = (
        re.search(r'Invoice\s*:\s*(\S+)', text) or
        re.search(r'Rechnung\s*:\s*(\S+)', text) or
        re.search(r'τιμολόγιο\s*:\s*(\S+)', text)
    ).group(1) if any(re.search(pattern, text) for pattern in [r'Invoice\s*:', r'Rechnung\s*:', r'τιμολόγιο\s*:']) else "Not Found"

    details['Date'] = (
        re.search(r'Date\s*:\s*(\d{2}/\d{2}/\d{4})', text) or
        re.search(r'Datum\s*:\s*(\d{2}/\d{2}/\d{4})', text) or
        re.search(r'Ημερομηνία\s*:\s*(\d{2}/\d{2}/\d{4})', text)
    ).group(1) if any(re.search(pattern, text) for pattern in [r'Date\s*:', r'Datum\s*:', r'Ημερομηνία\s*:']) else "Not Found"

    details['Amount'] = (
        re.search(r'Total including taxes\s*:\s*([\d,\.]+\s*€)', text) or
        re.search(r'Gesamtbetrag\s*:\s*([\d,\.]+\s*€)', text) or
        re.search(r'Σύνολο\s*:\s*([\d,\.]+\s*€)', text)
    ).group(1) if any(re.search(pattern, text) for pattern in [r'Total including taxes\s*:', r'Gesamtbetrag\s*:', r'Σύνολο\s*:']) else "Not Found"

    details['Company'] = (
        re.search(r'Company\s*:\s*(.*)', text) or
        re.search(r'Firma\s*:\s*(.*)', text) or
        re.search(r'Εταιρεία\s*:\s*(.*)', text)
    ).group(1) if any(re.search(pattern, text) for pattern in [r'Company\s*:', r'Firma\s*:', r'Εταιρεία\s*:']) else "Not Found"

    return details