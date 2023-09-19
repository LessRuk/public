from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from settings import base_url


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = base_url

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"THe {locator} is not found.")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"THe {locator} is not found.")


class MainFormLocators:
    LOC_BAR = (By.XPATH, "//header/div[1]/div[2]/div[1]")
    LOC_LOGOUT = (By.XPATH, "//div[@id='logout-btn']")


class MainFormHelper(Base):
    def main_form_bar_check(self):
        all_list = self.find_elements(MainFormLocators.LOC_LOGOUT)
        res = [item.text for item in all_list]
        return res

