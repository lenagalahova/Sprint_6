import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            self.click(self.locators.cookie_button)
        except Exception:
            pass

    @allure.step("Кликнуть на вопрос с индексом")
    def click_question(self, index):
        question_locator = (
            self.locators.question_button[0],
            self.locators.question_button[1].format(index),
        )
        self.scroll_to_element(question_locator)
        self.click_js(question_locator)

    @allure.step("Получить текст ответа на вопрос с индексом")
    def get_answer_element(self, index):
        answer_locator = (
            self.locators.answer_text[0],
            self.locators.answer_text[1].format(index),
        )
        self.wait_visible(answer_locator)
        return self.get_text(answer_locator)

    @allure.step("Кликнуть на верхнюю кнопку 'Заказать'")
    def click_to_order_button(self):
        self.click(self.locators.order_button)

    @allure.step("Кликнуть на нижнюю кнопку 'Заказать'")
    def click_to_order_button_2(self):
        self.click(self.locators.order_button_2)
