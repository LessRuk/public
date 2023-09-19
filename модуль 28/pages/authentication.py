from selenium.webdriver.common.by import By
from pages.main import Base
from settings import base_url


class AuthLocators:
    LOC_auth_LOGIN_FIELD = (By.ID, "username")
    LOC_auth_PASS_FIELD = (By.ID, "password")
    LOC_auth_BUTTON = (By.ID, "kc-login")
    LOC_auth_ERROR = (By.ID, "form-error-message")
    LOC_AGREEMENT_FORM_LINK = (By.XPATH, '/html/body/div[1]/footer/div[1]/div[2]/a/span[2]')

    LOC_auth_OUT_BUTTON = (By.XPATH, "//div[@id='logout-btn']")
    LOC_auth_OUT_RES = (By.XPATH, "//h1[contains(text(),'Авторизация')]")
    LOC_auth_PHONE = (By.ID, "t-btn-tab-phone")
    LOC_auth_MAIL = (By.ID, "t-btn-tab-mail")
    LOC_auth_LOGIN = (By.ID, "t-btn-tab-login")


class AuthFormHelper(Base):
    def click_on_auth_button(self):
        return self.find_element(AuthLocators.LOC_auth_BUTTON, time=2).click()

    def enter_by_login(self, login):
        tab_login = self.find_element(AuthLocators.LOC_auth_LOGIN)
        tab_login.click()
        login_field = self.find_element(AuthLocators.LOC_auth_LOGIN_FIELD)
        login_field.send_keys(login)
        return login_field

    def send_password(self, password):
        password_field = self.find_element(AuthLocators.LOC_auth_PASS_FIELD)
        password_field.send_keys(password)
        return password_field

    def check_error(self):
        message = self.find_element(AuthLocators.LOC_auth_ERROR, time=2)
        return message

    def into_agreements(self):
        try:
            self.driver.get(base_url)
            self.find_element(AuthLocators.LOC_AGREEMENT_FORM_LINK, time=2).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
        except Exception as ex:
            print(ex)

    def into_agreements_second_link(self):
        try:
            self.driver.get(base_url)
            self.find_element(AuthLocators.LOC_AGREEMENT_FORM_LINK_2, time=2).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
        except Exception as ex:
            print(ex)

    def logout_button(self):
        return self.find_element(AuthLocators.LOC_auth_OUT_BUTTON, time=2).click()

    def check_logout(self):
        out_elements = self.find_elements(AuthLocators.LOC_auth_OUT_RES)
        res = [el.text for el in out_elements]
        return res
