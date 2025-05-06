class BillingService:
    def calculate(self, df):
        df['Billable Amount'] = df['Hours'] * df['Rate']
        return df