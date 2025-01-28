from app.core.extract import is_invoice, extract_invoice_details
from app.pipelines.feature_pipeline import feature_extraction

def run_inference(file_path: str) -> dict:
    """Pipeline to run inference on a file."""
    text = feature_extraction(file_path)
    invoice_status = is_invoice(text)
    details = extract_invoice_details(text) if invoice_status else {}
    return {"is_invoice": invoice_status, "details": details}
