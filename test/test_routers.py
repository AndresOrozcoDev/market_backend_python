from fastapi.testclient import TestClient

from main import app 


client = TestClient(app)


######################################### Main #########################################
def test_root():
    headers = {'api_key': 'development'}
    response = client.get('/', headers=headers)
    assert response.status_code == 200
    assert response.json() == {'message': "Welcome to Market Backend Project with Python and FastAPI!. Please add '/docs' to url"}


######################################### Supermarket #########################################
def test_create_supermarket():
    headers = {'api-key': 'development'}
    response = client.post('/supermarket?name=name', headers=headers)
    assert response.status_code == 200
    assert response.json() == {'message': 'Supermarket created', 'data': 'name'}


######################################### Category #########################################
def test_create_category():
    headers = {'api-key': 'development'}
    response = client.post('/category?name=name', headers=headers)
    assert response.status_code == 200
    assert response.json() == {'message': 'Category created', 'data': 'name'}