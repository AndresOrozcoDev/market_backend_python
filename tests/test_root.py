from fastapi.testclient import TestClient

from main import app 


client = TestClient(app)


def test_root():
    headers = {'api-key': 'development'}
    response = client.get('/', headers=headers)
    assert response.status_code == 200
    assert response.json() == {'message': "Welcome to Market Backend Project with Python and FastAPI!. Please add '/docs' to url"}