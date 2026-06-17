
class Asserter:

    @staticmethod
    def element_visible(element, text):
        assert text in element.text_content()

    @staticmethod
    def verify_text(element, text):
        assert element.text_content() == text