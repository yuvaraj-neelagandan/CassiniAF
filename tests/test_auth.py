import requests
import allure
import pytest


@allure.feature("Auth")
@allure.story("Valid Registration")
@pytest.mark.smoke
def test_valid_login(base_url):
    url = f"{base_url}/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert "token" in response.json()



@allure.feature("Auth")
@allure.story("Invalid Registration")
@pytest.mark.smoke
def test_invalid_login(base_url):
    url = f"{base_url}/register"
    payload = {
        "email": "eve.holt@reqres.in"
        # password intentionally missing
    }

    with allure.step("Sending invalid registration request"):
        response = requests.post(url, json=payload)
        print("INVALID login response:", response.status_code, response.text)

    with allure.step("Validating error for missing password"):
        assert response.status_code == 400
        assert "error" in response.json()
