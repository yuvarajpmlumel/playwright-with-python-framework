from playwright.sync_api import expect

class Search:
    def __init__(self, page):
        self.page = page
        self.search_icon = '//span[@aria-label="Search"]'
        self.search_field = '//input[@class="input search-input"]'
        self.search_count = "//span[@class='search-count']"
    
    def click_search(self):
        self.page.click(self.search_icon)

    def check_search_bar_displayed(self):
        search_locator = self.page.locator(self.search_field)  # Store the locator
        expect(search_locator).to_have_count(1), "Search bar not present or multiple similar items present"

    def check_search_bar_not_displayed(self):
        search_locator = self.page.locator(self.search_field)  # Store the locator
        expect(search_locator).to_have_count(0), "Search bar displayed unexpectedly"

    def searchValue(self, searchNumber):
        self.page.click(self.search_field)
        self.page.fill(self.search_field, searchNumber)  # or use .type() if needed
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(2000)  # 2 seconds in milliseconds

    def check_for_equality(self, expected):
        search_count_text = self.page.locator(self.search_count).inner_text()
        
        if search_count_text != "Not found":
            split_array = search_count_text.split("of")
            actual = split_array[1].strip()
            assert expected == actual, f"Expected '{expected}', but got '{actual}'"
        else:
            assert expected == search_count_text, f"Expected '{expected}', but got '{search_count_text}'"
