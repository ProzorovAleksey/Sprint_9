import allure
import pytest
from pathlib import Path
from faker import Faker
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium import webdriver

import config
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




@pytest.fixture
@allure.title("подключаем удаленный/локальный драйвер в зависимости от настройки конфига")
def remote_driver():
    if config.remote_driver:
        options = ChromeOptions()
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "128.0")
        options.set_capability("selenoid:options", {"enableVNC": True})
        options.set_capability("selenoid:options", {"enableVideo": False})

        remote_driver = webdriver.Remote(command_executor='http://selenoid:4444/wd/hub', options=options)
    else:
        remote_driver = webdriver.Chrome()

    yield remote_driver
    remote_driver.quit()
