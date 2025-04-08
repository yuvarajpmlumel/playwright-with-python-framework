from pages.Home.search import Search
from appURL import appURL
import pytest

@pytest.fixture(autouse=True)
def before_each(launch_url):
    launch_url(appURL.SANITY)

@pytest.mark.sanity
def test_BarEnable_Disable(page):
    searchbar = Search(page)
    # Navigate to the website
    searchbar.click_search()
    searchbar.check_search_bar_displayed()

    searchbar.click_search()
    searchbar.check_search_bar_not_displayed()

    print("All tests passed!")
