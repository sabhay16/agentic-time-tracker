from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from routes.api import router as api_router
from services.logging_service import setup_logging

app = FastAPI()

setup_logging()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple Token-based Auth Dependency
def verify_token(request: Request):
    token = request.headers.get("Authorization")
    if token != "Bearer secret-token":
        raise HTTPException(status_code=403, detail="Unauthorized")

app.include_router(api_router, prefix="/api", dependencies=[Depends(verify_token)])
from fastapi.security import HTTPBearer
from fastapi.openapi.models import APIKey

security = HTTPBearer()
app.include_router(api_router, prefix="/api", dependencies=[Depends(verify_token)], tags=["api"])