from fastapi.testclient import TestClient

from main import app 


client = TestClient(app)


def test_create_supermarket():
    headers = {'api-key': 'development'}
    response = client.post('/supermarket?name=name', headers=headers)
    assert response.status_code == 200
    assert response.json() == {'message': 'Supermarket created', 'data': 'name'}
