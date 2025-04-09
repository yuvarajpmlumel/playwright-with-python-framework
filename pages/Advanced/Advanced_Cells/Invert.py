from playwright.sync_api import Page

class Invert:
    def __init__(self, page: Page):
        self.page = page
        self.invert_sign_button = 'span#invertSignsMenu-b'

    def click_on_invert(self):
        self.page.locator(self.invert_sign_button).click()
        self.page.wait_for_timeout(1000)  # wait 1 second
