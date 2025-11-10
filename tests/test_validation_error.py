import requests
import allure
import random
import pytest

@allure.feature("Validation")
@allure.story("Missing Required Fields")
@pytest.mark.regression
def test_missing_required_fields(headers):
    url = "https://gorest.co.in/public/v2/users"
    payload = {"name": "John Doe"}  # Missing email, gender, status

    with allure.step("Sending request with missing required fields"):
        response = requests.post(url, json=payload, headers=headers)

    with allure.step("Validating response code and error content"):
        assert response.status_code == 422
        assert any("field" in str(err) for err in response.json())


@allure.feature("Validation")
@allure.story("Invalid Email Format")
@pytest.mark.regression
def test_invalid_email_format(headers):
    url = "https://gorest.co.in/public/v2/users"
    payload = {
        "name": "John Doe",
        "email": "invalid-email",
        "gender": "male",
        "status": "active"
    }

    with allure.step("Sending request with invalid email"):
        response = requests.post(url, json=payload, headers=headers)

    with allure.step("Validating email format error"):
        assert response.status_code == 422
        assert any("email" in str(err).lower() for err in response.json())


@allure.feature("Validation")
@allure.story("Invalid Enum Values")
@pytest.mark.regression
def test_invalid_enum_values(headers):
    url = "https://gorest.co.in/public/v2/users"
    payload = {
        "name": "John Doe",
        "email": f"wrong_enum_{random.randint(1000,9999)}@example.com",
        "gender": "other",
        "status": "maybe"
    }

    with allure.step("Sending request with invalid gender/status values"):
        response = requests.post(url, json=payload, headers=headers)

    with allure.step("Validating enum value error messages"):
        assert response.status_code == 422
        assert any("gender" in str(err).lower() or "status" in str(err).lower() for err in response.json())


@allure.feature("Error")
@allure.story("Invalid URL")
@pytest.mark.smoke
def test_invalid_url():
    url = "https://jsonplaceholder.typicode.com/invalid-endpoint"

    with allure.step("Accessing an invalid endpoint"):
        response = requests.get(url)

    with allure.step("Expecting 404 Not Found"):
        assert response.status_code == 404


@allure.feature("Error")
@allure.story("Method Not Allowed")
@pytest.mark.smoke
def test_method_not_allowed():
    url = "https://httpbin.org/get"

    with allure.step("Trying DELETE on a GET endpoint"):
        response = requests.delete(url)

    with allure.step("Expecting 405 Method Not Allowed"):
        assert response.status_code == 405
