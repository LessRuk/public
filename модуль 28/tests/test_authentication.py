import random

from pages.authentication import AuthFormHelper
from pages.main import MainFormHelper
from pages.agreement import AgreeFormHelper

from settings import Valid_CRDNT
from settings import Invalid_CRDNT


class TestSuite_Auth():
    def go_to_login_form(browser):
        login_form = AuthFormHelper(browser)
        auth_check = MainFormHelper(browser)
        login_form.go_to_site()
        return login_form, auth_check

    def go_to_login_form_for_error(browser):
        login_form = AuthFormHelper(browser)
        auth_check = AuthFormHelper(browser)
        login_form.go_to_site()
        return login_form, auth_check

    def check_success_login(login_form, auth_check):
        login_form.click_on_auth_button()
        element = auth_check.main_form_bar_check()
        assert "Выйти" in element

    def get_error_message(login_form, auth_check):
        login_form.click_on_auth_button()
        message = auth_check.check_error()
        return message.text

    # Авторизация по логину
    def test_auth_by_login_positive(self, browser):
        login_form, auth_check = TestSuite_Auth.go_to_login_form(browser)
        login_form.enter_by_login(Valid_CRDNT['rt_login'])
        login_form.send_password(Valid_CRDNT['rt_pass'])
        TestSuite_Auth.check_success_login(login_form, auth_check)

    # Авторизация по номеру телефона
    def test_auth_by_number_positive(self, browser):
        login_form, auth_check = TestSuite_Auth.go_to_login_form(browser)
        login_form.enter_by_login(Valid_CRDNT['phone'])
        login_form.send_password(Valid_CRDNT['rt_pass'])
        TestSuite_Auth.check_success_login(login_form, auth_check)

    # Авторизация по email
    def test_auth_by_mail_positive(self, browser):
        login_form, auth_check = TestSuite_Auth.go_to_login_form(browser)
        login_form.enter_by_login(Valid_CRDNT['email'])
        login_form.send_password(Valid_CRDNT['rt_pass'])
        TestSuite_Auth.check_success_login(login_form, auth_check)

    # Проверка работы логаута c рандомным способом логина
    def test_logout(self, browser):
        login_form, auth_check = TestSuite_Auth.go_to_login_form(browser)
        elementsOfTuple = ('rt_login', 'phone', 'email')
        login_by = random.choice(elementsOfTuple)
        login_form.enter_by_login(Valid_CRDNT[login_by])
        login_form.send_password(Valid_CRDNT['rt_pass'])
        TestSuite_Auth.check_success_login(login_form, auth_check)
        login_form.logout_button()
        assert "Авторизация" in login_form.check_logout()

    # Авторизация c неверным логином
    def test_auth_by_login_negative(self, browser):
        login_form, auth_check = TestSuite_Auth.go_to_login_form_for_error(browser)
        login_form.enter_by_login(Invalid_CRDNT['rt_login'])
        login_form.send_password(Valid_CRDNT['rt_pass'])
        assert TestSuite_Auth.get_error_message(login_form, auth_check) == "Неверный логин или пароль"

    # Авторизация с неверным номером телефона
    def test_auth_by_number_negative(self, browser):
        login_form, auth_check = TestSuite_Auth.go_to_login_form_for_error(browser)
        login_form.enter_by_login(Invalid_CRDNT['phone'])
        login_form.send_password(Valid_CRDNT['rt_pass'])
        assert TestSuite_Auth.get_error_message(login_form, auth_check) == "Неверный логин или пароль"

    # Авторизация с неверной почтой
    def test_auth_by_email_negative(self, browser):
        login_form, auth_check = TestSuite_Auth.go_to_login_form_for_error(browser)
        login_form.enter_by_login(Invalid_CRDNT['email'])
        login_form.send_password(Valid_CRDNT['rt_pass'])
        assert TestSuite_Auth.get_error_message(login_form, auth_check) == "Неверный логин или пароль"

    # Авторизация с неверным паролем
    def test_auth_by_invalid_password_negative(self, browser):
        login_form, auth_check = TestSuite_Auth.go_to_login_form_for_error(browser)
        login_form.enter_by_login(Valid_CRDNT['rt_login'])
        login_form.send_password(Invalid_CRDNT['rt_pass'])
        assert TestSuite_Auth.get_error_message(login_form, auth_check) == "Неверный логин или пароль"

    # Переход по ссылке  пользовательскому соглашению
    def test_check_link_to_agreement_form_by_link(self, browser):
        into_agree = AuthFormHelper(browser)
        agree_check = AgreeFormHelper(browser)
        into_agree.go_to_site()
        into_agree.into_agreements()
        header = agree_check.check_agreement_header()
        txt = 'Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»'
        assert txt  in list(header)
