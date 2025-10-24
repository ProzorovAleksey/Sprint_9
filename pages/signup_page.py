import allure

from locators.login_locators import LoginPageLocators
from locators.signup_locators import RegistrationPageLocators
from pages.base_page import BasePage


class SignUp(BasePage):

    @allure.step("Заполнить все поля формы регистрации")
    def fill_complete_registration_form(self, user_data):
        self.enter_text(RegistrationPageLocators.first_name, user_data["first_name"])
        self.enter_text(RegistrationPageLocators.last_name, user_data["last_name"])
        self.enter_text(RegistrationPageLocators.username, user_data["username"])
        self.enter_text(RegistrationPageLocators.reg_email, user_data["email"])
        self.enter_text(RegistrationPageLocators.reg_password, user_data["password"])

    @allure.step("Нажать финальную кнопку 'Создать аккаунт'")
    def click_final_create_account_button(self):
        self.click_element(RegistrationPageLocators.create_account_final_button)

    @allure.step("Проверить переход на страницу авторизации")
    def verify_redirect_to_login(self):
        self.wait_until_url_contains('signin')

    @allure.step("Проверить отображение формы авторизации")
    def verify_login_form_visible(self):
        assert self.find_visible_element(LoginPageLocators.email_field)
        assert self.find_visible_element(LoginPageLocators.password_field)
        assert self.find_visible_element(LoginPageLocators.enter_button_signin)

    @allure.step("Проверить успешную регистрацию")
    def verify_successful_registration(self):
        self.verify_redirect_to_login()
        self.verify_login_form_visible()
