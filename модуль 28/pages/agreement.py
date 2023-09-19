from selenium.webdriver.common.by import By
from pages.main import Base


class AgreementLocators:
    LOC_AGREEMENT_HEADER = (By.XPATH, "/html/body/div[1]/h1")


class AgreeFormHelper(Base):
    def check_agreement_header(self):
        all_list = self.find_elements(AgreementLocators.LOC_AGREEMENT_HEADER, time=2)
        return [x.text for x in all_list]
