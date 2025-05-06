import pandas as pd
from services.billing import BillingService

def test_calculate():
    df = pd.DataFrame([{"Hours": 10, "Rate": 150}])
    billing = BillingService()
    billed_df = billing.calculate(df)
    
    assert billed_df.iloc[0]["Billable Amount"] == 1500