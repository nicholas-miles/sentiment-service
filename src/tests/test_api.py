from fastapi.testclient import TestClient

from sentiment_service.api.main import app

client = TestClient(app)


def test_predict():
    resp = client.post("/predict", json={"text": "Amazing movie, loved it!"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["prediction"] in {
        "very positive",
        "positive",
        "neutral",
        "negative",
        "very negative",
    }
    assert 0.0 <= data["score"] <= 1.0


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
