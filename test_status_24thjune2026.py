from playwright.sync_api import APIRequestContext


def test_status_24thjune2026(before_each_test: APIRequestContext):
    response = before_each_test.get("https://simple-grocery-store-api.click/status")

    assert response.status == 200
    body = response.json()
    assert body["status"] == "UP"
