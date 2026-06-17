import re
from utils.logger import logger
class Healer:
    def generate_fallback_locators(self, old_locator):
        logger.info(f"Generating fallbacks for: {old_locator}") 
        keyword =  re.sub(r'[^a-zA-Z0-9]', ' ', old_locator)
        keyword = keyword.replace(" ", "")
        possible_candidates = [f"[placeholder=\"{keyword.capitalize()}\"]", f"[data-test-=\"{keyword}\"]"]
        return possible_candidates

    def heal(self, locator): 
        logger.info(f"Healing the locator {locator}")   
        fallback_strategies = self.generate_fallback_locators(locator)
        for fallback in fallback_strategies:
            if fallback:
                return fallback
        raise Exception(
            f"No fallback locators for {locator}"
        )
    
