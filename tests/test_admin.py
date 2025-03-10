from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_admin():
    response = client.get("/admin")
    assert response.status_code == 200

    response = client.get("/admin/book/list")
    assert response.status_code == 200

    response = client.get("/admin/book/details/1")
    assert response.status_code == 200
