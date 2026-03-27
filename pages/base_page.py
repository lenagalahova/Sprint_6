import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    @allure.step("Кликнуть по элементу")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Кликнуть по элементу через JavaScript")
    def click_js(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст в поле")
    def send_keys(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    @allure.step("Получить текст из элемента")
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Ожидать видимость элемента")
    def wait_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Скроллить до элемента")
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    @allure.step("Закрыть календарь нажатием ENTER")
    def close_calendar(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(Keys.ENTER)

    @allure.step("Открыть URL")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить количество открытых вкладок")
    def get_window_handles_count(self):
        """Возвращает количество открытых вкладок"""
        return len(self.driver.window_handles)

    @allure.step("Переключиться на последнюю вкладку")
    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ожидать открытия новой вкладки")
    def wait_for_new_tab(self, initial_handles_count):
        """Ожидает открытия новой вкладки"""

        def check_new_tab_opened(driver):
            return len(driver.window_handles) > initial_handles_count

        self.wait.until(check_new_tab_opened)

    @allure.step("Ожидать, что URL содержит: {text}")
    def wait_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))
