from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_items_all():
    response = client.get("/items")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_items_filtered():
    response = client.get("/items?q=apple")
    assert response.status_code == 200
    data = response.json()
    assert all("apple" in item["name"].lower() for item in data)
