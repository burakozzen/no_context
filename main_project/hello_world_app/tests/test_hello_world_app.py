from main_project.hello_world_app.hello_world_app import app
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World Burak !"


@pytest.mark.parametrize("item_id,expected_status_code, expected_result", [
    (0, 422, "Input should be greater than 0"),
    (2, 422, "Input should be less than 2")
])
def test_get_item_failed(item_id: int, expected_status_code: int, expected_result: str):
    response = client.get(f"/get_item/{item_id}")
    assert response.status_code == expected_status_code
    response_dict = response.json()
    assert response_dict['detail'][0]['msg'] == expected_result


@pytest.mark.parametrize("item_id,expected_status_code, expected_result", [
    (1, 200, {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    })
])
def test_get_item_success(item_id: int, expected_status_code: int, expected_result: dict):
    response = client.get(f"/get_item/{item_id}")
    assert response.status_code == expected_status_code
    response_dict = response.json()
    assert response_dict == expected_result
