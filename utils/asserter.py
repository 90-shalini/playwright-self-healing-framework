
class Asserter:

    @staticmethod
    def element_visible(element, text):
        print(element.text_content())
        assert text in element.text_content()

    @staticmethod
    def verify_text(element, text):
        print(element.text_content())
        assert element.text_content() == text