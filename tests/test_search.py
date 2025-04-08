from pages.Home.search import Search
import pytest
@pytest.fixture(autouse=True)
def before_each():
    print("➡️ Runs before each test")
    yield

def test_search(page):
    searchbar = Search(page)
    # Navigate to the website
    searchbar.click_search()
    searchbar.check_search_bar_displayed()

    searchbar.click_search()
    searchbar.check_search_bar_not_displayed()

    print("All tests passed!")

# // "IS_HEADLESS=true
# BASE_URL=https://demo.playwright.dev/todomvc/
# VIEWPORT_WIDTH=1270
# VIEWPORT_HEIGHT=709 " from this .env  , remove width and height . i would like make some changes . base-rl : i will give just an base url and endpoints are given in test script on beforeAll () . can it is possible. BeforeAll has endpoint and it should use fixture . on fixture , base url from env and endpoint , use it to goto 