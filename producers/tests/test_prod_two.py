from fastapi.testclient import TestClient
from producers.onboard_info_gen import app

test_producer = TestClient(app)


def test_health():
    response = test_producer.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}
