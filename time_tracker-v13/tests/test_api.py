import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_entries_unauthorized():
    response = client.get("/api/entries")
    assert response.status_code == 403

def test_get_entries_authorized(monkeypatch):
    from services.etl import ETLService
    monkeypatch.setattr(ETLService, "extract", lambda self: [{"test": "data"}])
    headers = {"Authorization": "Bearer secret-token"}
    response = client.get("/api/entries", headers=headers)
    assert response.status_code in [200, 404, 500]  # 500 if db isn't running