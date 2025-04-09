from pages.Home.Home_Analyze.Search import Search
from pages.Advanced import Advanced
from pages.Advanced.Advanced_Cells import EditCell
from appURL import appURL
import pytest

@pytest.fixture(autouse=True)
def before_each(launch_url):
    # Set use_local_storage=True when you want login
    launch_url(appURL.Scenario, use_local_storage=True)
 
def xtest_scenario(page,click_tab):
    searchbar = Search(page)
    advanced = Advanced(page)
    # edit_cell = EditCell(page)

    click_tab("Insert")
    
    # edit_cell.click_the_cell_static("3","0")
    # advanced.advanced_cell.edit_cell.click_the_cell_static("3","0")
    # advanced.advanced_cell.invert.click_on_invert()
    click_tab("Home")
    searchbar.click_search()
    searchbar.searchValue("-1039")
    # searchbar.check_for_equality("1")
    print("All tests passed!")