class AnomalyDetector:
    def detect(self, timesheet_df):
        anomalies = timesheet_df[timesheet_df['hours'] > 12]
        return anomalies.to_dict(orient="records")