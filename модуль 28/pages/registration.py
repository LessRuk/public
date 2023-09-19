from selenium.webdriver.common.by import By
from pages.main import Base
from settings import base_url


class RegLocators:
    LOC_REGISTRATION = (By.XPATH, "//a[@id='kc-register']")
    LOC_REG_FIELD_NEW_MAIL = (By.XPATH, "//input[@id='address']")
    LOC_REG_FIELD_PASS = (By.XPATH, "//input[@id='password']")
    LOC_REG_FIELD_CONFPASS = (By.XPATH, "//input[@id='password-confirm']")
    LOC_REG_AGREEMENTS_LINK = (By.LINK_TEXT, "пользовательского соглашения")
    LOC_REG_ALERT = (By.XPATH, "//h2[contains(text(),'Учётная запись уже существует')]")
    LOC_REG_FIRST_NAME_ERROR = (By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")
    LOC_REG_SECOND_NAME_ERROR = (By.XPATH,"//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]")
    LOC_REG_FIELD_FIIRST_NAME = (By.XPATH,
                                 "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]")
    LOC_REG_FIELD_SECOND_NAME = (By.XPATH,
                                 "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]")
    LOC_REG_BUTTON = (By.XPATH,"//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/button[1]")


class RegFormHelper(Base):
    def push_to_registration(self):
        return self.find_element(RegLocators.LOC_REGISTRATION, time=3).click()

    def enter_first_name(self, first_name):
        first_name_field = self.find_element(RegLocators.LOC_REG_FIELD_FIIRST_NAME)
        first_name_field.send_keys(first_name)
        return first_name_field

    def enter_second_name(self, second_name):
        second_name_field = self.find_element(RegLocators.LOC_REG_FIELD_SECOND_NAME)
        second_name_field.send_keys(second_name)
        return second_name_field

    def enter_mail(self, mail):
        mail_field = self.find_element(RegLocators.LOC_REG_FIELD_NEW_MAIL)
        mail_field.send_keys(mail)
        return mail_field

    def enter_number(self, number):
        number_field = self.find_element(RegLocators.LOC_REG_FIELD_NEW_MAIL)
        number_field.send_keys(number)
        return number_field

    def enter_pass(self, password):
        pass_field = self.find_element(RegLocators.LOC_REG_FIELD_PASS)
        pass_field.send_keys(password)
        return pass_field

    def enter_confpass(self, confpassword):
        cpass_field = self.find_element(RegLocators.LOC_REG_FIELD_CONFPASS)
        cpass_field.send_keys(confpassword)
        return cpass_field

    def click_on_button(self):
        return self.find_element(RegLocators.LOC_REG_BUTTON, time=3).click()

    def check_first_name_ERR(self):
        short_message = self.find_element(RegLocators.LOC_REG_FIRST_NAME_ERROR)
        return short_message

    def check_second_name_ERR(self):
        short_message = self.find_element(RegLocators.LOC_REG_SECOND_NAME_ERROR)
        return short_message

    def from_registration_to_agreement(self):
        try:
            self.driver.get(base_url)
            self.find_element(RegLocators.LOC_REG_AGREEMENTS_LINK, time=2).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
        except Exception as ex:
            print(ex)

    def check_alert(self):
        free_message = self.find_element(RegLocators.LOC_REG_ALERT)
        return free_message
