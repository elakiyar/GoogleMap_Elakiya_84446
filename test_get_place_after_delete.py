from playwright.sync_api import APIRequestContext
import pytest
import json

filepath = "C:\\June2026_batch2_playwright_APITesting\\24thJune2026\\24thJune2026_GoogleMap\\global_gm.json"

@pytest.mark.order(6)
@pytest.mark.dependency(scope="session", depends=["delete_place"])
def test_get_place_after_delete(before_each_test: APIRequestContext):
    with open(filepath, "r") as file:
        data = json.load(file)

    place_id = data["place_id"]
    key = data["key"]

    response = before_each_test.get(f"https://rahulshettyacademy.com/maps/api/place/get/json?place_id={place_id}&key={key}")

    assert response.status == 404
    print(json.dumps(response.json(), indent=4))
