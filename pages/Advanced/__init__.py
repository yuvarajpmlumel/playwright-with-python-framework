from pages.Advanced.Advanced_Cells import Advanced_Cells
from playwright.sync_api import Page

class Advanced:
    def __init__(self, page: Page):
        self.page = page
        self._advanced_cell = None

    @property
    def advanced_cell(self):
        if self._advanced_cell is None:
            self._advanced_cell = Advanced_Cells(self.page)
        return self._advanced_cell
