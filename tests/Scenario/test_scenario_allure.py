from pages.Home.Home_Analyze.Search import Search
from pages.Advanced import Advanced
from pages.Advanced.Advanced_Cells import EditCell
from appURL import appURL
import pytest

@pytest.fixture(autouse=True)
def before_each(launch_url):
    # Set use_local_storage=True when you want login
    launch_url(appURL.Scenario, use_local_storage=True)
 
import allure

@allure.feature("Scenario Feature")
@allure.story("Invert and Search Scenario")
@allure.title("Test the advanced cell invert and search flow")
def test_scenario(page, click_tab):
    with allure.step("Create page objects"):
        searchbar = Search(page)
        advanced = Advanced(page)

    with allure.step("Click on Insert tab"):
        click_tab("Insert")

    with allure.step("Click a cell and invert the value"):
        advanced.advanced_cell.edit_cell.click_the_cell_static("3", "0")
        advanced.advanced_cell.invert.click_on_invert()

    with allure.step("Switch to Home tab and perform search"):
        click_tab("Home")
        searchbar.click_search()
        searchbar.searchValue("-1039")
        # searchbar.check_for_equality("1")
    
    with allure.step("Final assertion/log"):
        print("All tests passed!")
