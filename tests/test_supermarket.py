from fastapi.testclient import TestClient

from main import app 


client = TestClient(app)


def test_get_supermarket_by_id():
    headers = {'api-key': 'development'}
    response = client.get('/supermarket/1', headers=headers)
    assert response.status_code == 200
    assert response.json() == { 'message': 'Get Supermarket success', 'data': {'name': 'testname', 'id': 1 }}

def test_create_supermarket():
    headers = {'api-key': 'development'}
    response = client.post('/supermarket?name=name', headers=headers)
    assert response.status_code == 200
    assert response.json() == {'message': 'Supermarket created', 'data': 'name'}

def test_update_supermarket():
    headers = {'api-key': 'development'}
    response = client.put('/supermarket/1?name=testname', headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Supermarked updated"}
