import data
from locators.login_locators import LoginPageLocators
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):

    @allure.step('Выполняем вход в систему')
    def login(self):
        self.enter_text(LoginPageLocators.email_field, data.User.LOG_DATA_NAME)
        self.enter_text(LoginPageLocators.password_field, data.User.LOG_DATA_PASSWORD)
        self.click_element(LoginPageLocators.enter_button_signin)

    @allure.step('Проверяем успешный вход')
    def verify_successful_login(self):
        self.wait_until_url_contains('recipes')
        self.wait_for_text_in_element(LoginPageLocators.button_exit, 'Выход')

    @allure.step('Проверяем видимость поля email')
    def is_email_field_visible(self):
        return self.find_visible_element(LoginPageLocators.email_field).is_displayed()

    @allure.step('Проверяем видимость поля пароля')
    def is_password_field_visible(self):
        return self.find_visible_element(LoginPageLocators.password_field).is_displayed()



