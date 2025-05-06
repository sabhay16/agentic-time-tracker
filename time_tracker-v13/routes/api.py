from fastapi import APIRouter, Request
from config import DATABASE_URL
from services.etl import ETLService
from ai_agents.openai_timesheet_agent import TimesheetAgent
import pandas as pd
import sqlalchemy

router = APIRouter()
etl_service = ETLService()
agent = TimesheetAgent()
engine = sqlalchemy.create_engine(DATABASE_URL)

@router.get("/entries")
def get_entries():
    with engine.connect() as conn:
        df = pd.read_sql("SELECT * FROM time_entries LIMIT 50", conn)
        return df.to_dict(orient="records")

@router.post("/suggest")
def suggest_entry(req: Request):
    payload = await req.json()
    context = payload.get("context", "")
    suggestion = agent.suggest_entries(context)
    return suggestion

from fastapi import UploadFile, File
from services.parser_service import TimesheetParser

@router.post("/upload-timesheet")
async def upload_timesheet(file: UploadFile = File(...)):
    contents = await file.read()
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(contents)
    
    parser = TimesheetParser()
    try:
        parsed = parser.parse(temp_path)
        return {"filename": file.filename, "parsed": parsed}
    except Exception as e:
        return {"error": str(e)}