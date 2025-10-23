from selenium.webdriver.common.by import By

class LoginPageLocators:

    email_field = (By.NAME, "email")
    password_field = (By.NAME, 'password')
    enter_button_signin = (By.CSS_SELECTOR, "button.style_button__1FFWl.styles_button__1jD3X.style_button_style_dark-blue__1cpq7")
    button_exit = (By.XPATH, ".//*[text()='Выход']")
