
import pytest
from playwright.sync_api import Browser, Page
from dotenv import load_dotenv
import os
import json

# Load variables from .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")

@pytest.fixture(scope="function")
def launch_url(page: Page):
    def _navigate(endpoint: str, use_local_storage=False):
        page.set_viewport_size({"width": 1270, "height": 709})

        full_url = f"{BASE_URL}{endpoint}"
        if use_local_storage:
            try:
                with open("local.json", "r") as f:
                    local_storage = json.load(f)

                # Prepare and inject localStorage
                script_lines = [
                    f'window.localStorage.setItem("{key}", {json.dumps(value)});'
                    for key, value in local_storage.items()
                ]
                script = "\n".join(script_lines)
                page.context.add_init_script(script)
                print("✅ localStorage injected")

                # 👇 Extra precaution: open a blank page first to ensure script runs
                page.goto("about:blank")
                page.wait_for_timeout(500)  # wait 0.5s to be extra safe
                page.goto(full_url, timeout=60000)
                page.wait_for_timeout(5000)

            except FileNotFoundError:
                print("⚠️ local.json not found. Skipping localStorage injection.")
        else:
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