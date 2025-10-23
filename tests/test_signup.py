import allure

from data import Url
from pages.signup_page import SignUp


class TestSignUp:
    @allure.suite('Регистрация')

    def test_registration_using_complete_method(self, driver, create_user):

        sign_up =SignUp(driver)

        with allure.step("Открыть страницу регистрации"):
            sign_up.open_page(Url.REG_URL)

        with allure.step("Выполнить полную регистрацию пользователя"):
            sign_up.fill_complete_registration_form(create_user)

        with allure.step("Нажимаем на кнопку 'Создать аккаунт'"):
            sign_up.click_final_create_account_button()

        with allure.step("Проверить успешность регистрации"):
            sign_up.verify_successful_registration()
