from playwright.sync_api import APIRequestContext
import pytest
import json

filepath = "C:\\June2026_batch2_playwright_APITesting\\GoogleMap\\global_gm.json"

@pytest.mark.order(1)
@pytest.mark.dependency(scope="session", name="add_place")
def test_add_place(before_each_test: APIRequestContext):
    with open(filepath, "r") as file:
        data = json.load(file)

    payload = {
        "location": {
            "lat": -38.383494,
            "lng": 33.427362
        },
        "accuracy": 50,
        "name": "BajajFinSer",
        "phone_number": "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": ["shoe park", "shop"],
        "website": "http://google.com",
        "language": "French-IN"
    }

    response = before_each_test.post("/maps/api/place/add/json", data=payload)

    assert response.status == 200
    print(json.dumps(response.json(), indent=4))
    data['place_id'] = response.json()["place_id"]
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)
