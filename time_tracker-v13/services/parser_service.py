import pandas as pd
import docx
import pdfplumber
import os

class TimesheetParser:
    def parse(self, file_path):
        ext = os.path.splitext(file_path)[-1].lower()
        if ext in [".xls", ".xlsx"]:
            return self._parse_excel(file_path)
        elif ext == ".docx":
            return self._parse_word(file_path)
        elif ext == ".pdf":
            return self._parse_pdf(file_path)
        else:
            raise ValueError("Unsupported file type")

    def _parse_excel(self, file_path):
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")

    def _parse_word(self, file_path):
        doc = docx.Document(file_path)
        data = []
        for table in doc.tables:
            for row in table.rows:
                data.append([cell.text.strip() for cell in row.cells])
        return data

    def _parse_pdf(self, file_path):
        data = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    data.extend(text.splitlines())
        return data