import pytest
from fastapi.testclient import TestClient
from main import app
import database
@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def clean_db():
    database.reset_db()
    # после теста ничего не делаем, так как reset_db уже очистила

def test_create_task(client):
    payload = {"title": "Купить молоко"}
    response = client.post("/tasks", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Купить молоко"
    assert data["id"] == 1
    assert data["completed"] is False