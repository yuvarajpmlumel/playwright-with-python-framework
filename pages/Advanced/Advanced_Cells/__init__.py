from playwright.sync_api import Page
from .Invert import Invert
from .EditCell import EditCell

class Advanced_Cells:
    def __init__(self, page: Page):
        self.page = page
        self._invert = None
        self._edit_cell = None

    @property
    def invert(self):
        if self._invert is None:
            self._invert = Invert(self.page)
        return self._invert

    @property
    def edit_cell(self):
        if self._edit_cell is None:
            self._edit_cell = EditCell(self.page)
        return self._edit_cell
