from fastapi import Depends
from fastapi.testclient import TestClient
from main import app, properties

async def new_properties(x: int=0, y: int=1):
    return {"from": x, "to": y}

app.dependency_overrides[properties] = new_properties

client = TestClient(app)

def test_overridden_depends():
    response = client.get("/persons/")
    assert response.status_code == 200
    assert response.json() == [
  {
    "name": "Tom",
    "age": 20
  }
]

