# Description: This file contains the main FastAPI application and the Streamlit interface.

from fastapi import FastAPI
from app.api.endpoints import router
import streamlit as st
from app.pipelines.inference_pipeline import run_inference

app = FastAPI()
app.include_router(router)

def streamlit_interface():
    st.title("Invoice Reader and Extractor")
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file:
        file_path = f"/tmp/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        result = run_inference(file_path)
        if result["is_invoice"]:
            st.success("This file is an invoice.")
            st.json(result["details"])
        else:
            st.error("This file is not recognized as an invoice.")

        os.remove(file_path)

if __name__ == "__main__":
    st.set_page_config(page_title="Invoice Extractor")
    streamlit_interface()