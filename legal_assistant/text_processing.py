#text_preprocessing.py
import PyPDF2
from pdfminer.high_level import extract_text as pdfminer_extract_text
import docx
import os
import pytesseract
from PIL import Image
import io

def process_document(file_path):
    _, file_extension = os.path.splitext(file_path)
    
    if file_extension.lower() == '.pdf':
        return process_pdf(file_path)
    elif file_extension.lower() == '.docx':
        return process_docx(file_path)
    elif file_extension.lower() == '.txt':
        return process_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

def process_pdf(file_path):
    try:
        # Try PyPDF2 first
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
        
        # If PyPDF2 fails to extract text, use pdfminer
        if not text.strip():
            text = pdfminer_extract_text(file_path)
        
        # If both fail, try OCR
        if not text.strip():
            text = ocr_pdf(file_path)
        
        if not text.strip():
            raise ValueError("Unable to extract text from PDF")
        
        return text
    except Exception as e:
        raise ValueError(f"Error processing PDF document: {str(e)}")

def ocr_pdf(file_path):
    try:
        from pdf2image import convert_from_path
        
        images = convert_from_path(file_path)
        if not images:
            raise ValueError("No images found in the PDF for OCR")
        
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image)
        return text
    except Exception as e:
        raise ValueError(f"Error performing OCR on PDF: {str(e)}")


def process_docx(file_path):
    try:
        doc = docx.Document(file_path)
        return " ".join([paragraph.text for paragraph in doc.paragraphs])
    except Exception as e:
        raise ValueError(f"Error processing DOCX document: {str(e)}")

def process_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        raise ValueError(f"Error processing TXT document: {str(e)}")