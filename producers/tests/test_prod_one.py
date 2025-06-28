from fastapi.testclient import TestClient
from producers.rocket_data_gen import app

test_producer = TestClient(app)

def test_ping():
    response = test_producer.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}
    