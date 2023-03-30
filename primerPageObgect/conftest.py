import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def browsser():
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    yield driver
    driver.quit()