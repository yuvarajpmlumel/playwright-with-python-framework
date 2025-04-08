from playwright.sync_api import expect

class Search:
    def __init__(self, page):
        self.page = page
        self.search_icon = '//span[@aria-label="Search"]'
        self.search_field = '//input[@class="input search-input"]'
    
    def click_search(self):
        self.page.click(self.search_icon)

    def check_search_bar_displayed(self):
        search_locator = self.page.locator(self.search_field)  # Store the locator
        expect(search_locator).to_have_count(1), "Search bar not present or multiple similar items present"

    def check_search_bar_not_displayed(self):
        search_locator = self.page.locator(self.search_field)  # Store the locator
        expect(search_locator).to_have_count(0), "Search bar displayed unexpectedly"
