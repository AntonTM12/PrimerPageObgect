from selenium.webdriver.common.by import By


from .base_page import BassPage

class YaSearchLocators:
    LOCATOR_YA_SER_FIELD = (By.ID, "text")
    LOCATOR_YA_SER_BUTON = (By.XPATH, "//button[contains(text(),'Найти')]")

class SearchHelper(BassPage):
    def enter_word(self, word):
        search_field = self.find_element(YaSearchLocators.LOCATOR_YA_SER_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_poisk(self):
        return self.find_element(YaSearchLocators.LOCATOR_YA_SER_BUTON, time=2).click()


