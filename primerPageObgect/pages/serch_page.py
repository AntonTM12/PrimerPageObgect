from selenium.webdriver.common.by import By
from .ya_pages import SearchHelper
from .ya_pages import YaSearchLocators
from .base_page import BassPage

class YaSearchPageLocators:
    LOCATOR_YA_NAVI_BAR = (By.CSS_SELECTOR, ".service__name")

class SerchPageHelper(BassPage):
    def check_navi_bar(self):
        all_list = self.find_elements(YaSearchPageLocators.LOCATOR_YA_NAVI_BAR)
        return [x.text for x in all_list]
