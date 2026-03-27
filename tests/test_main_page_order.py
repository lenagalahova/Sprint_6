import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from pages.main_pages_questions import MainHomePage
from pages.main_pages_order import OrderPage
from data import (
    URL,
    my_name_1,
    my_surname_1,
    my_adress_1,
    my_tel_1,
    my_data_1,
    my_name_2,
    my_surname_2,
    my_adress_2,
    my_tel_2,
    my_data_2,
)


class TestOrderFlow:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.epic("Яндекс.Самокат")
    @allure.feature("Оформление заказа")
    @pytest.mark.parametrize(
        "name, surname, adress, tel, data",
        [
            (my_name_1, my_surname_1, my_adress_1, my_tel_1, my_data_1),
            (my_name_2, my_surname_2, my_adress_2, my_tel_2, my_data_2),
        ],
    )
    @allure.title("Оформление заказа с разными наборами данных")
    @allure.description(
        "Проверка, что заказ можно оформить с разными данными пользователя"
    )
    def test_order_track(self, name, surname, adress, tel, data):
        self.driver.get(URL)
        home_page_question = MainHomePage(self.driver)
        home_page_question.accept_cookies()
        home_page_question.click_to_order_button()
        order_page = OrderPage(self.driver)
        order_page.fill_my_data_1_step(name, surname, adress, tel)
        order_page.click_next_button()
        order_page.fill_my_data_2_step(data)
        order_page.click_order_button_2()
        order_page.wait_popup_order()
        order_page.click_to_yes_button()
        order_page.wait_text_of_order()
        text = order_page.get_text_of_order()
        assert "Заказ оформлен" in text

    @allure.title("Переход на главную страницу по клику на логотип 'Самоката'")
    @allure.description(
        "Проверка, что при клике на логотип 'Самоката' происходит переход на главную страницу"
    )
    def test_click_scooter_logo_redirects_to_main_page(self):
        self.driver.get(URL)
        scooter_link = OrderPage(self.driver)
        scooter_link.click_to_header_logo_scooter()
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title("Открытие Дзена в новой вкладке по клику на логотип Яндекса")
    @allure.description(
        "Проверка, что при клике на логотип Яндекса открывается страница Дзена в новой вкладке"
    )
    def test_click_ya_logo_redirects_to_yandex(self):
        self.driver.get(URL)
        scooter_link = OrderPage(self.driver)
        scooter_link.click_to_header_logo_yandex()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_contains("dzen.ru")
        )
        assert "dzen.ru" in self.driver.current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
