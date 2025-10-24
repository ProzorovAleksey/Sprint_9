from locators.recipe_card_locators import CardPageLocators
from pages.create_recipe_page import CreateRecipePage
from data import Url
import allure

from pages.login_page import LoginPage


class TestCreateRecipe:
    @allure.suite("При создании рецепта осуществляется переход к карточке созданного рецепта")
    def test_create_recipe_jump_to_recipe_card_page(self, remote_driver, picture_path):
        login_page = LoginPage(remote_driver)

        with allure.step('Открываем страницу логина и авторизуемся'):
            login_page.open_page(Url.LOG_URL)
            login_page.login()
            login_page.verify_successful_login()

        recipe_page = CreateRecipePage(remote_driver)

        with allure.step('Переходим на страницу создания рецепта'):
            recipe_page.open_page(Url.CREATE_RECIPE_URL)

        with allure.step('Создаем рецепт'):
            recipe_page.create_recipe(picture_path)
            recipe_page.wait_for_recipe_page_load()

        with allure.step('Проверяем результат'):
            recipe_page.wait_until_url_contains('recipes')
            name = recipe_page.get_element_text(CardPageLocators.recipe_name_title)
            is_button_visible = recipe_page.is_add_to_shopping_list_button_visible()

        assert 'Картошечка' in name
        assert is_button_visible
