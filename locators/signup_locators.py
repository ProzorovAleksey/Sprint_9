from selenium.webdriver.common.by import By

class RegistrationPageLocators:

    first_name = (By.NAME, "first_name")
    last_name = (By.NAME, "last_name")
    username = (By.NAME, "username")
    reg_email = (By.NAME, "email")
    reg_password = (By.NAME, 'password')

    create_account_final_button = (By.XPATH, "//button[text()='Создать аккаунт']")


