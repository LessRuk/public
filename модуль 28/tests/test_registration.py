import pytest

from pages.registration import RegFormHelper
from pages.agreement import AgreeFormHelper
from settings import Valid_CRDNT


class Testsuite_authentication():
    input_params = [
        # Проверка на длину короче 2х символов
        ("ё", "Необходимо заполнить поле кириллицей. От 2 до 30 символов."),

        # Проверка на длину более 30 символов
        ("ё" * 31, "Необходимо заполнить поле кириллицей. От 2 до 30 символов."),

        # Проверка на длину более 30 символов (максимально в PYTEST + кодировка ё=\u0451 )
        ("ё" * (32767 // 7), "Необходимо заполнить поле кириллицей. От 2 до 30 символов."),

        # Проверка на ввод спец.символов
        ('!@#$%' * 5, "Необходимо заполнить поле кириллицей. От 2 до 30 символов."),

        # Проверка на латиницу
        ("Gala" * 5, "Необходимо заполнить поле кириллицей. От 2 до 30 символов."),

        # Проверка на спецсимволы в кириллице (В начале)
        ("!Галя", "Необходимо заполнить поле кириллицей. От 2 до 30 символов."),

        # Проверка на спецсимволы в кириллице (В конце)
        ("Галя_", "Необходимо заполнить поле кириллицей. От 2 до 30 символов."),

        # Проверка на спецсимволы в кириллице (В середине)
        ("Г_а_л_и_н_а", "Необходимо заполнить поле кириллицей. От 2 до 30 символов."),
    ]
    test_id = [f'field_value={x[0]}' for x in input_params]

    # Форма регистрации полe "Имя"
    @pytest.mark.parametrize('name_value, message_text', input_params, ids=test_id)
    def test_reg_first_name_field(self, browser, name_value, message_text):
        first_name = RegFormHelper(browser)
        first_name.go_to_site()
        first_name.push_to_registration()
        first_name.enter_first_name(name_value)
        first_name.click_on_button()
        message = first_name.check_first_name_ERR()
        assert message.text == message_text

    # Форма регистрации полe "Фамилия"
    @pytest.mark.parametrize('name_value, message_text', input_params, ids=test_id)
    def test_reg_second_name_field(self, browser, name_value, message_text):
        second_name = RegFormHelper(browser)
        second_name.go_to_site()
        second_name.push_to_registration()
        second_name.enter_second_name(name_value)
        second_name.click_on_button()
        message = second_name.check_second_name_ERR()
        assert message.text == message_text

    # Регистрация Повторное использование данных

    @pytest.mark.parametrize('reg_by', [
        #   Повторное использование уже занятого телефона
        'phone',
        #   Повторное использование уже занятого email
        'email'
    ])
    def test_reg_free_mail(self, browser, reg_by):
        registration_form = RegFormHelper(browser)
        registration_form.go_to_site()
        registration_form.push_to_registration()
        registration_form.enter_first_name("Галя")
        registration_form.enter_second_name("ГаляГаля")
        if reg_by == 'email':
            registration_form.enter_mail(Valid_CRDNT['email'])
        if reg_by == 'phone':
            registration_form.enter_number(Valid_CRDNT['phone'])
        registration_form.enter_pass(Valid_CRDNT['rt_pass'])
        registration_form.enter_confpass(Valid_CRDNT['rt_pass'])
        registration_form.click_on_button()
        alert = registration_form.check_alert()
        assert alert.text == "Учётная запись уже существует"

    # Переход к пользовательскому соглашению c формы регистрации
    def test_check_link_to_agreement_from_registration_form(self, browser):
        reg_form = RegFormHelper(browser)
        agree_check = AgreeFormHelper(browser)
        reg_form.go_to_site()
        reg_form.push_to_registration()
        reg_form.from_registration_to_agreement()
        header = agree_check.check_agreement_header()
        txt = 'Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»'
        assert txt in list(header)
