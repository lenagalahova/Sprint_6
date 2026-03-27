from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import (
    question_button,
    answer_text,
    cookie_button,
    order_button,
)


class MainHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)
        self.question_button_template = question_button
        self.answer_text_template = answer_text
        self.cookie_button = cookie_button
        self.order_button = order_button

    def accept_cookies(self):
        try:
            cookie = self.wait.until(
                expected_conditions.element_to_be_clickable(self.cookie_button)
            )
            cookie.click()
        except Exception:
            pass

    def get_question_element(self, index):
        by_question, value_question = self.question_button_template
        return self.driver.find_element(by_question, value_question.format(index))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_question(self, index):
        self.accept_cookies()
        question = self.get_question_element(index)
        self.scroll_to_element(question)
        by_question, value_question = self.question_button_template
        self.wait.until(
            expected_conditions.element_to_be_clickable(
                (by_question, value_question.format(index))
            )
        )
        self.driver.execute_script("arguments[0].click();", question)

    def get_answer_element(self, index):
        by_answer, value_answer = self.answer_text_template
        return self.driver.find_element(by_answer, value_answer.format(index))

    def wait_answer_text(self, index):
        by_answer, value_answer = self.answer_text_template
        self.wait.until(
            expected_conditions.visibility_of_element_located(
                (by_answer, value_answer.format(index))
            )
        )

    def get_answer_text(self, index):
        self.wait_answer_text(index)
        answer = self.get_answer_element(index)
        return answer.text

    def click_to_order_button(self):
        self.driver.find_element(*self.order_button).click()

    def click_to_order_button_2(self):
        self.driver.find_element(*self.order_button_2).click()
