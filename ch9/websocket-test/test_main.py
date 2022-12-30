from fastapi.testclient import TestClient
from .main import app
def test_wstest():
    client = TestClient(app)
    with client.websocket_connect("/wstest") as websocket:
        data = websocket.receive_json()
        assert data == {"msg": "WebSocket Server"}