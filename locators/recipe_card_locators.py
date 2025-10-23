from selenium.webdriver.common.by import By

class CardPageLocators:
    button_add = (By.XPATH, ".//*[text()=' Добавить в покупки']")
    recipe_name_title = (By.TAG_NAME, 'h1')