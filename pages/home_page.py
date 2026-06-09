from pages.base_page import BasePage
from playwright.sync_api import sync_playwright, expect
from utils.asserter import Asserter
from locators.home_page import HomePageLocators

class HomePage(BasePage):

    def logout(self):
        self.click(HomePageLocators.menu_btn)
        self.click(HomePageLocators.logout_option)

    def add_product_to_cart(self):
        self.click(HomePageLocators.add_to_cart_btn)
        element = self.page.locator(HomePageLocators.cart_icon)
        Asserter.verify_text(element, "1")

    def remove_product_to_cart(self):
        self.click(HomePageLocators.add_to_cart_btn)
        element = self.page.get_by_text("Remove")
        element.click()
        # TODO Replace below and move it to assert class
        expect(self.page.locator(HomePageLocators.cart_icon)).to_have_count(0)

