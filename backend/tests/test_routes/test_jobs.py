import json


def test_create_job(client):
	data = {
			"title" : "FastAPI Developer",
			"company" : "Wipro",
			"company_url" : "https://www.wipro.com",
			"location" : "India",
			"description" : "We are hiring FastAPI Developers",
			"date_posted" : "2022-07-20"
		   }
	response = client.post("/job/create-job", json.dumps(data))
	assert response.status_code == 200
