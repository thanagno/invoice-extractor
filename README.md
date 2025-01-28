# Invoice Extractor

A Python-based application for reading and extracting key information from invoices in multiple languages (English, German, and Greek). The application supports feature extraction, training pipelines, and inference pipelines, and is accessible via both a Streamlit interface and a FastAPI backend.

## Features
- **Multi-language Support**: English, German, and Greek invoice processing.
- **Data Extraction**: Extracts key invoice details like Invoice Number, Date, Amount, and Company.
- **Streamlit Interface**: User-friendly frontend for uploading invoices.
- **FastAPI Backend**: API for processing invoices programmatically.
- **Dockerized Deployment**: Easily containerized for scalability.

## Directory Structure
```plaintext
invoice-extractor/
├── app/
│   ├── __init__.py
│   ├── main.py                # Entry point for FastAPI and Streamlit
│   ├── api/
│   │   ├── __init__.py
│   │   └── endpoints.py       # FastAPI routes
│   ├── pipelines/
│   │   ├── __init__.py
│   │   ├── feature_pipeline.py
│   │   ├── training_pipeline.py
│   │   └── inference_pipeline.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── extract.py         # Extraction logic for invoices
│   └── utils/
│       ├── __init__.py
│       └── pdf_utils.py       # Utilities for reading PDF files
├── Dockerfile                 # Docker instructions for containerization
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Installation
### Prerequisites
- Python 3.9 or newer
- Docker (optional)

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-repo/invoice-extractor.git
cd invoice-extractor
```

### Step 2: Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### Step 3: Run Locally
1. **Start the FastAPI Backend**:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
   Access the API at [http://localhost:8000/docs](http://localhost:8000/docs).

2. **Start the Streamlit Frontend**:
   ```bash
   streamlit run app/main.py
   ```
   Access the frontend at [http://localhost:8501](http://localhost:8501).

## Docker Deployment
### Build the Docker Image
```bash
docker build -t invoice-extractor .
```

### Run the Docker Container
```bash
docker run -p 8000:8000 -p 8501:8501 invoice-extractor
```

## Usage
### API Usage
1. Upload a PDF file to the `/process-invoice/` endpoint.
2. Receive structured invoice details in the response.

### Streamlit Interface
1. Upload a PDF invoice using the Streamlit UI.
2. View extracted details in an interactive interface.

## Future Enhancements
- Add support for more languages.
- Include advanced machine learning for better text extraction.
- Enhance security for processing sensitive documents.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

