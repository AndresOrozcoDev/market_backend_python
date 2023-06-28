from fastapi.testclient import TestClient

from main import app 


client = TestClient(app)


def test_create_category():
    headers = {'api-key': 'development'}
    response = client.post('/category?name=name', headers=headers)
    assert response.status_code == 200
    assert response.json() == {'message': 'Category created', 'data': 'name'}