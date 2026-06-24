from playwright.sync_api import APIRequestContext
import pytest
import json

filepath = "C:\\June2026_batch2_playwright_APITesting\\GoogleMap\\global_gm.json"

@pytest.mark.order(2)
@pytest.mark.dependency(scope="session", depends=["add_place"])
def test_get_place(before_each_test: APIRequestContext):
    with open(filepath, "r") as file:
        data = json.load(file)

    place_id = data["place_id"]
    key = data["key"]

    response = before_each_test.get(f"/maps/api/place/get/json?place_id={place_id}&key={key}")

    assert response.status == 200
    print(json.dumps(response.json(), indent=4))
