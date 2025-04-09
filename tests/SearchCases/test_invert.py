from pages.Home.Home_Analyze.Search import Search
from pages.Advanced.Advanced_Cells.EditCell import EditCell
from pages.Advanced.Advanced_Cells.Invert import Invert
from appURL import appURL
import pytest
from pages.Advanced import Advanced_Cells

@pytest.fixture(autouse=True)
def before_each(launch_url):
    launch_url(appURL.Search)
 
def test_BarEnable_Disable(page,click_tab):
    searchbar = Search(page)
    editcell = EditCell(page)
    invert = Invert(page)

    click_tab("Insert")
    editcell.click_the_cell_static("3","0")
    invert.click_on_invert()

    click_tab("Home")
    searchbar.click_search()
    searchbar.searchValue("-1039")
    searchbar.check_for_equality("1")
    print("All tests passed!")
