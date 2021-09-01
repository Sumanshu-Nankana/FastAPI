import json


def test_create_job(client, normal_user_token_headers):
    data = {
        "title": "FastAPI Developer",
        "company": "Wipro",
        "company_url": "https://www.wipro.com",
        "location": "India",
        "description": "We are hiring FastAPI Developers",
        "date_posted": "2022-07-20",
    }
    response = client.post(
        "/job/create-job", json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 200


def test_retrieve_job_by_id(client):
    data = {
        "title": "FastAPI Developer",
        "company": "Wipro",
        "company_url": "https://www.wipro.com",
        "location": "India",
        "description": "We are hiring FastAPI Developers",
        "date_posted": "2022-07-20",
    }
    client.post("/job/create-job", json.dumps(data))
    response = client.get("/job/get/1")
    assert response.status_code == 200
    assert response.json()["title"] == "FastAPI Developer"
