import allure
from selenium import webdriver
from pages.main_pages_questions import MainHomePage
from data import URL


class TestMainPageQuestion:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.epic("Яндекс.Самокат")
    @allure.feature("Вопросы о важном")
    @allure.title("Проверка ответа на вопрос 1")
    def test_open_question_0(self):
        self.driver.get(URL)

        home_page_question = MainHomePage(self.driver)
        home_page_question.click_question(0)
        text_0 = home_page_question.get_answer_text(0)
        assert text_0 == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    @allure.title("Проверка ответа на вопрос 2")
    def test_open_question_1(self):
        home_page_question_1 = MainHomePage(self.driver)
        home_page_question_1.click_question(1)
        text_1 = home_page_question_1.get_answer_text(1)
        assert (
            text_1
            == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        )

    @allure.title("Проверка ответа на вопрос 3")
    def test_open_question_2(self):
        home_page_question_2 = MainHomePage(self.driver)
        home_page_question_2.click_question(2)
        text_2 = home_page_question_2.get_answer_text(2)
        assert (
            text_2
            == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        )

    @allure.title("Проверка ответа на вопрос 4")
    def test_open_question_3(self):
        home_page_question_3 = MainHomePage(self.driver)
        home_page_question_3.click_question(3)
        text_3 = home_page_question_3.get_answer_text(3)
        assert (
            text_3 == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        )

    @allure.title("Проверка ответа на вопрос 5")
    def test_open_question_4(self):
        home_page_question_4 = MainHomePage(self.driver)
        home_page_question_4.click_question(4)
        text_4 = home_page_question_4.get_answer_text(4)
        assert (
            text_4
            == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        )

    @allure.title("Проверка ответа на вопрос 6")
    def test_open_question_5(self):
        home_page_question_5 = MainHomePage(self.driver)
        home_page_question_5.click_question(5)
        text_5 = home_page_question_5.get_answer_text(5)
        assert (
            text_5
            == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        )

    @allure.title("Проверка ответа на вопрос 7")
    def test_open_question_6(self):
        home_page_question_6 = MainHomePage(self.driver)
        home_page_question_6.click_question(6)
        text_6 = home_page_question_6.get_answer_text(6)
        assert (
            text_6
            == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        )

    @allure.title("Проверка ответа на вопрос 8")
    def test_open_question_7(self):
        home_page_question_7 = MainHomePage(self.driver)
        home_page_question_7.click_question(7)
        text_7 = home_page_question_7.get_answer_text(7)
        assert (
            text_7 == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        )

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
