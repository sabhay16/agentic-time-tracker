import pandas as pd
from services.etl import ETLService

def test_normalize_data():
    data = {"consultant": ["Alice"], "client": ["Acme"], "Date": ["2025-01-01"], "Hours": [8], "rate": [100]}
    df = pd.DataFrame(data)
    file_path = "mock.csv"
    df.to_csv(file_path, index=False)
    
    etl = ETLService()
    normalized = etl.normalize_data(file_path, "Platform A")
    
    assert list(normalized.columns) == ["Consultant", "Client", "Date", "Hours", "Rate"]
    assert normalized.iloc[0]["Hours"] == 8