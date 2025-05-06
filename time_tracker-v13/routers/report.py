from fastapi import APIRouter

router = APIRouter()

@router.get("/generate-invoice/")
def generate_invoice(client: str):
    return {"status": "Invoice generated"}