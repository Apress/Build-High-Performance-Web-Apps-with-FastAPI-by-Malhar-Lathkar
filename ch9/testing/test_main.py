from fastapi.testclient import TestClient
from fastapi import status
from .main import app
client = TestClient(app)


def test_list():
    response = client.get("/list/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"title":"Python", "price":500}

def test_addnew():
    response = client.post("/list", json={"title":"Learn FastAPI", "price":1000})
    assert response.status_code == status.HTTP_201_CREATED