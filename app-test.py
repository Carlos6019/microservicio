import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_devops_success(client):
    response = client.post('/DevOps', 
        headers={"X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"},
        json={
            "message": "This is a test",
            "to": "Juan Perez",
            "from": "Rita Asturia",
            "timeToLifeSec": 45
        }
    )
    assert response.status_code == 200
    assert response.json['message'] == "Hello Juan Perez your message will be send"

def test_devops_invalid_api_key(client):
    response = client.post('/DevOps', 
        headers={"X-Parse-REST-API-Key": "invalid_key"},
        json={
            "message": "This is a test",
            "to": "Juan Perez",
            "from": "Rita Asturia",
            "timeToLifeSec": 45
        }
    )
    assert response.status_code == 403
    assert response.data.decode() == "ERROR"

