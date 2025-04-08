
import pytest
from playwright.sync_api import Page
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")

@pytest.fixture(autouse=True)
def launch_url(page: Page):
    def _navigate(endpoint: str):
        page.set_viewport_size({"width": 1270, "height": 709})
        full_url = f"{BASE_URL}{endpoint}"
        page.goto(full_url, timeout=60000)
        return page
    return _navigate