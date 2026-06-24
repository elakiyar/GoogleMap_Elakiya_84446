from playwright.sync_api import APIRequestContext
import pytest
import json

filepath = "C:\\June2026_batch2_playwright_APITesting\\24thJune2026\\24thJune2026_GoogleMap\\global_gm.json"

@pytest.mark.order(3)
@pytest.mark.dependency(scope="session", depends=["add_place"], name="update_place")
def test_update_place(before_each_test: APIRequestContext):
    with open(filepath, "r") as file:
        data = json.load(file)

    place_id = data["place_id"]
    key = data["key"]

    payload = {
        "place_id": place_id,
        "address": "SKNTechSolutions, Pune, Maharashtra, India",
        "key": key
    }

    response = before_each_test.put("https://rahulshettyacademy.com/maps/api/place/update/json", params={"key": key}, data=payload)

    assert response.status == 200
    print(json.dumps(response.json(), indent=4))
