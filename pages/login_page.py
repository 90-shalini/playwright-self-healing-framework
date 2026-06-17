from pages.base_page import BasePage
from utils.asserter import Asserter
from locators.login_page import LoginLocators

class LoginPage(BasePage):

    def login(self, username, password):
        self.fill(LoginLocators.username_text, username)
        self.fill(LoginLocators.password_text, password)
        self.click(LoginLocators.login_btn)

    def verify_error(self, error_message):
        error_label_element= self.page.locator(LoginLocators.error_label)
        Asserter.element_visible(error_label_element, error_message)

    def verify_login(self):
        assert "inventory" in self.page.url

    def verify_logout(self, logo_text):
        logo_element= self.page.locator(LoginLocators.logo_element)
        print(logo_text)
        Asserter.element_visible(logo_element, logo_text)




        