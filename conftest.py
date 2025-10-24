import allure
import pytest
from pathlib import Path
from faker import Faker
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
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



REMOTE_DRIVER = True

@pytest.fixture
@allure.title("подключаем удаленный/локальный драйвер в зависимости от настройки конфига")
def driver():
    if REMOTE_DRIVER:
        options = Options()
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "128.0")  # ИСПРАВЛЕНО: 128.0 вместо 120.0
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": False
        })

        driver = webdriver.Remote(
            command_executor='http://selenoid:4444/wd/hub',
            options=options
        )
    else:
        # Локальный драйвер
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()
