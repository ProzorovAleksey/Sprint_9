import allure

from data import Url
from pages.login_page import LoginPage


class TestAuthorization:

    @allure.suite('Авторизация')
    def test_successful_authorization(self, remote_driver):

        login_page = LoginPage(remote_driver)

        with allure.step("Открываем страницу входа"):
            login_page.open_page(Url.LOG_URL)

        with allure.step("Проверим видимость полей email и Пароль"):
            login_page.is_email_field_visible()
            login_page.is_password_field_visible()

        with allure.step("Заполняем поля и нажимаем 'Войти'"):
            login_page.login()

        with allure.step("Проверяем успешный вход"):
            login_page.verify_successful_login()