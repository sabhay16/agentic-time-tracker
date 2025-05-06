import os
import pandas as pd
import docx
import pdfplumber

def parse_excel(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")

def parse_word(file_path):
    doc = docx.Document(file_path)
    lines = [para.text for para in doc.paragraphs if para.text.strip()]
    return lines

def parse_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.splitlines()

def parse_timesheet(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext in ['.xls', '.xlsx']:
        return parse_excel(file_path)
    elif ext == '.docx':
        return parse_word(file_path)
    elif ext == '.pdf':
        return parse_pdf(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")