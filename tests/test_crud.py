import requests
import allure
import random
import string
import pytest


@allure.feature("CRUD")
@allure.story("Create User")
@pytest.mark.regression
def test_create_user(headers):
    url = "https://gorest.co.in/public/v2/users"
    email = f"testuser_{random.randint(1000, 9999)}@example.com"
    payload = {
        "name": "QA Automation Bot",
        "email": email,
        "gender": "male",
        "status": "active"
    }

    with allure.step("Sending request to create user"):
        response = requests.post(url, json=payload, headers=headers)

    with allure.step("Validating user creation response"):
        assert response.status_code == 201
        json_resp = response.json()
        assert json_resp["email"] == email
        assert json_resp["name"] == "QA Automation Bot"


@allure.feature("CRUD")
@allure.story("Get Single Post")
@pytest.mark.smoke
def test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    with allure.step("Fetching single post by ID"):
        response = requests.get(url)

    with allure.step("Validating response for post retrieval"):
        assert response.status_code == 200
        data = response.json()
        assert "id" in data and data["id"] == 1
        assert isinstance(data["userId"], int)
        assert isinstance(data["title"], str)
