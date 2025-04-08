from playwright.sync_api import Page

class EditCell:
    def __init__(self, page: Page):
        self.page = page

    def click_the_cell_static(self, row_name: str, column_number: str):
        """
        Scroll to the specified cell and click it.
        :param row_name: The row name (string/ID)
        :param column_number: The column number (as string)
        """
        id_string = f"table-row-{row_name}_table-col-{column_number}"
        selector = f'(//div[@id="{id_string}"])[1]'

        # Assuming you have a reusable scroll method, else remove next line
        self.scroll_to_exact_row_and_column(row_name, column_number)

        self.page.locator(selector).click()

    def scroll_to_exact_row_and_column(self, row_name: str, column_number: str):
        # Dummy scroll function - implement your actual logic here
        self.page.evaluate(
            f'''
            () => {{
                const el = document.getElementById("table-row-{row_name}_table-col-{column_number}");
                if (el) el.scrollIntoView({{ behavior: "smooth", block: "center" }});
            }}
            '''
        )
