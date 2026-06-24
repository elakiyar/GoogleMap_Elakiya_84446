import json
import pytest

filepath = "C:\\June2026_batch2_playwright_APITesting\\24thJune2026\\24thJune2026_GoogleMap\\global_gm.json"

with open(filepath, "r") as file:
    data = json.load(file)


@pytest.fixture(scope="function")
def before_each_test(playwright):
    request = playwright.request.new_context(base_url=data["base_url"])

    yield request
    request.dispose()