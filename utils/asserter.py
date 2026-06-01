
class Asserter:
    def __init__(self, page):
        self.page = page

    def element_visible(self, locator, text):
        element = self.page.locator(locator)
        print(element.text_content())
        assert text in element.text_content()
        # expect(self.page.locator).to_be_visible()s