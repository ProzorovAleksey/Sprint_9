import allure

from locators.create_recipe_locators import RecipePageLocators
from locators.recipe_card_locators import CardPageLocators
from pages.base_page import BasePage
from data import Recipe


class CreateRecipePage(BasePage):
    @allure.step("Вводим название рецепта")
    def enter_recipe_name(self):
        self.enter_text(RecipePageLocators.recipe_name_field, Recipe.recipe_name)

    @allure.step("Вводим название ингредиента")
    def enter_recipe_ingredient_name(self):
        self.enter_text(RecipePageLocators.ingredient_name_field, Recipe.recipe_ingredient_name)
        self.click_element(RecipePageLocators.ingredient_list_item)

    @allure.step("Вводим необходимое количество ингредиента")
    def enter_recipe_weight(self):
        self.enter_text(RecipePageLocators.ingredient_weight_field, Recipe.recipe_ingredient_weight)

    @allure.step("Вводим время приготовления")
    def enter_recipe_time(self):
        self.enter_text(RecipePageLocators.time_field, Recipe.recipe_time)

    @allure.step("Нажимаем на кнопку добавления ингредиента")
    def click_on_add_ingredient_button(self):
        self.click_element(RecipePageLocators.ingredient_add_button)

    @allure.step("Вводим описание рецепта")
    def enter_description(self):
        self.enter_text(RecipePageLocators.description_field, Recipe.recipe_description)

    @allure.step("Загружаем картинку")
    def enter_picture(self, picture_path):
        self.upload_image(RecipePageLocators.load_picture_input, picture_path)

    @allure.step("Нажимаем на кнопку Создать рецепт")
    def click_on_create_recipe_button(self):
        self.scroll_to_bottom()
        self.click_element(RecipePageLocators.create_recipe_button)

    @allure.step("Создаем рецепт")
    def create_recipe(self, picture_path):
        self.enter_recipe_name()
        self.enter_recipe_ingredient_name()
        self.enter_recipe_weight()
        self.click_on_add_ingredient_button()
        self.enter_recipe_time()
        self.enter_description()
        self.enter_picture(picture_path)
        self.click_on_create_recipe_button()

    @allure.step("Проверяем видимость кнопки добавления в список покупок")
    def is_add_to_shopping_list_button_visible(self):
        try:
            return self.find_visible_element(CardPageLocators.button_add, timeout=10)
        except Exception as e:
            print("Ошибка определения видимости кнопки добавления: ", e)
            return False

    @allure.step("Ожидаем загрузку страницы рецепта")
    def wait_for_recipe_page_load(self):
        self.find_present_element(CardPageLocators.recipe_name_title)
        self.find_present_element(CardPageLocators.button_add)