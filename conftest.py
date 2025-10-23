import allure
import pytest
from pathlib import Path
from faker import Faker
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver

from data import Recipe


@pytest.fixture
def create_user():
    fake = Faker()
    user_data = {
        "email": fake.email(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "password": fake.password(),
        "username": fake.user_name()
    }
    return user_data

@pytest.fixture
def picture_path():
    path = Path(Recipe.recipe_pic_catalog)
    if path.exists():
        return str(path.absolute())
    else:
        pytest.skip(f"Test image {path} not found")


REMOTE_DRIVER = False   # признак использования удаленного WebDriver из Селеноида при запуске в docker-контейнере


@pytest.fixture
@allure.title("Подключаем удаленный или локальный драйвер в зависимости от флага REMOTE_DRIVER")
def driver():
    if REMOTE_DRIVER:
        options = ChromeOptions()
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "114.0")
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": False
        })

        driver = webdriver.Remote(
            command_executor='http://selenoid:4444/wd/hub',
            options=options
        )
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    yield driver
    driver.quit()
