import pandas as pd

class ETLService:
    def normalize_data(self, file_path, source):
        df = pd.read_excel(file_path) if file_path.endswith(".xlsx") else pd.read_csv(file_path)
        if source == "Platform A":
            df.rename(columns={"consultant": "Consultant", "client": "Client", "rate": "Rate"}, inplace=True)
        return df[["Consultant", "Client", "Date", "Hours", "Rate"]]