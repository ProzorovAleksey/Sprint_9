from selenium.webdriver.common.by import By

class RecipePageLocators:
    recipe_name_field = (By.XPATH, ".//div[text()='Название рецепта']/../input")
    ingredient_name_field = (By.XPATH, ".//div[text()='Ингредиенты']/../input")
    ingredient_list_item = (By.XPATH, ".//div[contains(@class, 'ingredientsInput')]/div[contains(@class, 'styles_container')]")
    ingredient_add_button = (By.XPATH, ".//div[text()='Добавить ингредиент']")
    ingredient_weight_field = (By.XPATH, ".//input[contains(@class, 'ingredientsAmountValue')]")
    time_field = (By.XPATH, ".//div[text()='Время приготовления']/../input")
    description_field = (By.XPATH, ".//div[text()='Описание рецепта']/../textarea")
    load_picture_input = (By.XPATH, ".//input[@type='file']")
    create_recipe_button = (By.XPATH, ".//button[text()='Создать рецепт']")
