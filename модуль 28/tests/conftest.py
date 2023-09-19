import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

