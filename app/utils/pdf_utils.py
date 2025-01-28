from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF file."""
    reader = PdfReader(file_path)
    return "".join([page.extract_text() for page in reader.pages])