import allure
import pytest
from selenium import webdriver
from pages.main_pages_questions import MainHomePage
from data import questions_data
from config import URL


class TestMainPageQuestion:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(URL)

    @allure.epic("Яндекс.Самокат")
    @allure.feature("Вопросы о важном")
    @allure.title("Проверка ответа на вопрос 1")
    @pytest.mark.parametrize("question_data", questions_data)
    def test_question_answer(self, question_data):
        main_page = MainHomePage(self.driver)
        main_page.accept_cookies()
        main_page.click_question(question_data["index"])
        actual_answer = main_page.get_answer_element(question_data["index"])
        assert actual_answer == question_data["answer"]

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
