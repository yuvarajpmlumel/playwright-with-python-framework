
import pytest
from playwright.sync_api import Page

# Load variables from .env file


@pytest.fixture(scope="function", autouse=True)
def setup_page(page: Page):
    page.set_viewport_size({"width": 1270, "height": 709})
    page.goto(
    "https://inforiverwebtest-dev.azurewebsites.net/?csvLocation=Sanity.csv&config=Sanity.json&URLLoad=true",
    timeout=90000  # timeout in milliseconds (60 seconds)
)
    yield page