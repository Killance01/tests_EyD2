from backend.main import app, get_exchange_rate
from fastapi.testclient import TestClient

def fake_exchange_rate():
    return 5000

client = TestClient(app)

def test_price_with_mock():
    app.dependency_overrides[get_exchange_rate] = fake_exchange_rate
    response = client.get("/price/10")
    data = response.json()

    assert response.status_code == 200
    assert data["usd"] == 10
    assert data["rate"] == 5000
    assert data["cop"] == 50000

    app.dependency_overrides.clear()
