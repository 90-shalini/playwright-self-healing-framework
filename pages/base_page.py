from utils.logger import logging


class BasePage:
    def __init__(self, page):
        self.page = page
        logging.info(f"Page initiated {self.page}")

    def click(self, locator):
        self.page.locator(locator).click()
        logging.info(f"Clicked locator: , {locator}")

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)
        logging.info(f"Entered text= {text} in locator = {locator}.")

