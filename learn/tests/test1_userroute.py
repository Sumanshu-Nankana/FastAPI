from fastapi.testclient import TestClient

import sys
import os
import json

# file = os.path.abspath(__file__)
# print(f"The value os current file is __file__ : {file}")

# parent_dir = os.path.dirname(file)
# print(f"The value of patent_dir is : {parent_dir}")

# parent_parent_dir = os.path.dirname(parent_dir)
# print(f"The value of parent_parent_dir is : {parent_parent_dir}")

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)


def test_create_user():
    data = {"email": "test1@test.com", "password": "test1pass"}
    response = client.post("/user", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "test1@test.com"
    assert response.json()["is_active"] == True
