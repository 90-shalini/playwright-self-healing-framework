from utils.logger import logging
from utils.healer import Healer

class BasePage:
    def __init__(self, page):
        self.page = page
        logging.info(f"Page initiated {self.page}")

    def find(self, locator):
        try:
            locator_obj = self.page.locator(locator)
            locator_obj.wait_for(state="visible", timeout=2000)
            return locator_obj
        except Exception:
            logging.info("Healing required.....")
            healed_locator = (
                Healer()
                .heal(locator)
            
        )
            print("Healed locator", healed_locator)
        return self.page.locator(
            healed_locator
        )

    def click(self, locator):
        self.page.locator(locator).click()
        logging.info(f"Clicked locator: , {locator}")

    def fill(self, locator, text):
        locator_obj = self.find(locator)
        locator_obj.fill(text)
        logging.info(f"Entered text= {text} in locator = {locator}.")

    