from pages.base_page import BasePage
from playwright.sync_api import sync_playwright, expect


class HomePage(BasePage):
    def logout(self):
        self.click("#react-burger-menu-btn")
        self.click("nav a#logout_sidebar_link")

    def add_product_to_cart(self):
        self.click("#add-to-cart-sauce-labs-bike-light")
        element = self.page.locator("#shopping_cart_container span")
        assert element.text_content() == '1'

    def remove_product_to_cart(self):
        self.click("#add-to-cart-sauce-labs-bike-light")

        # self.click("#remove-sauce-labs-backpack")
        element = self.page.get_by_text("Remove")
        element.click()
        expect(self.page.locator("#shopping_cart_container span")).to_have_count(0)
