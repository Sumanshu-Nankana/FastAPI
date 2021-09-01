import json


def test_create_user(client):
    data = {
        "username": "testuser1",
        "email": "user1@test.com",
        "password": "user1password",
    }
    response = client.post("/users/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "user1@test.com"
    assert response.json()["is_active"] == True
