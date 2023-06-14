from fastapi.testclient import TestClient

from main import app 


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World. Welcome to Market Backen Project with Python and FastAPI!. Please add '/docs' to url"}

def test_create_supermarket():
    params = {"name": "supermarket"}
    response = client.post("/api/supermarket", params=params)
    assert response.status_code == 200
    assert response.json() == {'message': 'Supermarket created', 'data': 'supermarket'}