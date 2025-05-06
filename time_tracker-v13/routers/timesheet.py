from fastapi import APIRouter

router = APIRouter()

@router.get("/timesheet/")
def get_timesheet():
    return {"message": "Timesheet endpoint"}