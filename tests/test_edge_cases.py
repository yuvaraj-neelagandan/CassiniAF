import requests
import allure
import random
import pytest


@allure.feature("Edge")
@allure.story("Empty Request Body")
@pytest.mark.regression
def test_empty_body(headers):
    url = "https://gorest.co.in/public/v2/users"
    response = requests.post(url, json={}, headers=headers)
    assert response.status_code == 422


@allure.feature("Edge")
@allure.story("Maximum Length Fields")
@pytest.mark.regression
def test_max_length_fields(headers):
    url = "https://gorest.co.in/public/v2/users"
    long_name = "A" * 255
    email = f"test_{long_name[:50]}@example.com"
    payload = {
        "name": long_name,
        "email": email,
        "gender": "male",
        "status": "active"
    }

    with allure.step("Sending request with max-length strings"):
        response = requests.post(url, json=payload, headers=headers)

    with allure.step("Validating boundary string handling"):
        assert response.status_code in [201, 422]


@allure.feature("Edge")
@allure.story("Unicode Characters")
@pytest.mark.regression
def test_unicode_characters(headers):
    url = "https://gorest.co.in/public/v2/users"
    payload = {
        "name": "José María González-Pérez £$%^",
        "email": f"unicode_{random.randint(1000, 9999)}@example.com",  # ASCII-safe
        "gender": "male",
        "status": "active"
    }

    with allure.step("Sending user with Unicode characters in name"):
        response = requests.post(url, json=payload, headers=headers)

    with allure.step("Validating Unicode character support in name"):
        assert response.status_code == 201
