from app.utils.pdf_utils import extract_text_from_pdf

def feature_extraction(file_path: str) -> str:
    """Pipeline to extract text features from a PDF."""
    return extract_text_from_pdf(file_path)