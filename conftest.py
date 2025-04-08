
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

@pytest.fixture
def click_tab(page: Page):
    def _click_tab(tab_name: str):
        # If not found, click fallback based on tab_name
        fallback_tab = f'//li[contains(@class,"tab-list-item")]//span[text()="{tab_name}"]'
        page.locator(fallback_tab).click()
        page.wait_for_timeout(2000)  # 2 seconds wait
    return _click_tab