from pages.Home.search import Search
from appURL import appURL
import pytest

@pytest.fixture(autouse=True)
def before_each(launch_url):
    launch_url(appURL.SANITY)

@pytest.mark.sanity
@pytest.mark.abc
def test_search(page):
    searchbar = Search(page)
    # Navigate to the website
    searchbar.click_search()
    searchbar.check_search_bar_displayed()

    searchbar.click_search()
    searchbar.check_search_bar_not_displayed()

    print("All tests passed!")

def xtest_search1(page):
    searchbar = Search(page)
    # Navigate to the website
    searchbar.click_search()
    searchbar.check_search_bar_displayed()

    searchbar.click_search1()
    searchbar.check_search_bar_not_displayed()

    print("All tests passed!")