import requests
import time
import pytest
import allure
from concurrent.futures import ThreadPoolExecutor

@allure.feature("Performance")
@allure.story("Response Time < 1s")
@pytest.mark.performance
def test_response_time_single():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    start = time.time()
    response = requests.get(url)
    duration = time.time() - start

    with allure.step("Validating single post response time"):
        assert response.status_code == 200
        assert duration < 1


@allure.feature("Performance")
@allure.story("Response Time for Collection < 1.5s")
@pytest.mark.performance
def test_response_time_collection():
    url = "https://jsonplaceholder.typicode.com/posts"
    start = time.time()
    response = requests.get(url)
    duration = time.time() - start

    with allure.step("Validating collection response time"):
        assert response.status_code == 200
        assert duration < 1.5


@allure.feature("Performance")
@allure.story("Concurrent Requests")
@pytest.mark.performance
def test_concurrent_requests():
    url = "https://httpbin.org/delay/1"
    with ThreadPoolExecutor(max_workers=10) as executor:
        start = time.time()
        futures = [executor.submit(requests.get, url) for _ in range(10)]
        results = [f.result() for f in futures]
        duration = time.time() - start

    with allure.step("Validating parallel request response times"):
        assert all(r.status_code == 200 for r in results)
        assert duration < 10  # Increased to 10s due to realistic delay


@allure.feature("Performance")
@allure.story("Stress Test 50 Requests")
@pytest.mark.performance
def test_stress_post():
    url = "https://httpbin.org/post"
    payload = {"data": "x" * 1024}
    success = 0

    for _ in range(50):
        try:
            r = requests.post(url, json=payload, timeout=3)
            if r.status_code == 200:
                success += 1
        except Exception:
            continue

    with allure.step("Validating success rate under load"):
        assert success >= 40  # 80% success tolerance
