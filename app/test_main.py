from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_fallen_soldiers():
    response = client.get("/table")
    assert response.status_code == 200
    print(response.text) 


