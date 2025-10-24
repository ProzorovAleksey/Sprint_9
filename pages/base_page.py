import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

class BasePage:
    @allure.title('Инициализируем драйвер')
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 15
        self.wait = WebDriverWait(self.driver, self.default_timeout)

    @allure.step('Открываем страницу по URL и ожидаем полной загрузки')
    def open_page(self, url):
        self.driver.get(url)
        return self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")


    @allure.step('Проверяем, что URL содержит указанную часть')
    def wait_until_url_contains(self, expected_url_part, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(expected_url_part)
        )

    @allure.step('Ищем элемент с ожиданием его видимости')
    def find_visible_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Ищем элемент с ожиданием его присутствия в DOM')
    def find_present_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Ищем скрытый элемент (без ожидания видимости)")
    def find_hidden_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Кликаем на элемент')
    def click_element(self, locator, timeout=30):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except ElementClickInterceptedException:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Вводим текст в поле')
    def enter_text(self, locator, text):
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)


    @allure.step('Получаем текст элемента')
    def get_element_text(self, locator):
        return self.find_visible_element(locator).text

    @allure.step('Ожидаем появления текста в элементе')
    def wait_for_text_in_element(self, locator, expected_text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, expected_text)
        )

    @allure.step("Скроллим страницу вниз")
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Загружаем изображение")
    def upload_image(self, locator, image_path):
        self.find_hidden_element(locator).send_keys(image_path)