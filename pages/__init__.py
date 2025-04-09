from .Advanced import Advanced
class Pages:
    def __init__(self, page):
        self.page = page
        self._advanced = None

    @property
    def edit_cell(self):
        if self._advanced is None:
            self._advanced = Advanced(self.page)
        return self._advanced