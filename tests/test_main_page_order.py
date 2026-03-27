import pytest
import allure
from selenium import webdriver
from pages.main_pages_questions import MainHomePage
from pages.pages_order import OrderPage
from config import URL
from data import (
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
        with allure.step("Открыть главную страницу и начать оформление заказа"):
            self.driver.get(URL)
            home_page = MainHomePage(self.driver)
            home_page.accept_cookies()
            home_page.click_to_order_button()
        with allure.step("Заполнить форму заказа"):
            order_page = OrderPage(self.driver)
            order_page.fill_my_data_1_step(name, surname, adress, tel)
            order_page.click_next_button()
            order_page.fill_my_data_2_step(data)
            order_page.click_order_button_2()
            order_page.click_to_yes_button()
        with allure.step("Проверить успешное оформление заказа"):
            text = order_page.get_text_of_order()
            assert "Заказ оформлен" in text

    @allure.title("Переход на главную страницу по клику на логотип 'Самоката'")
    @allure.description(
        "Проверка, что при клике на логотип 'Самоката' происходит переход на главную страницу"
    )
    def test_click_scooter_logo_redirects_to_main_page(self):
        main_page = MainHomePage(self.driver)
        order_page = OrderPage(self.driver)

        with allure.step("Открыть главную страницу"):
            main_page.open_url(URL)

        with allure.step("Кликнуть на логотип 'Самоката'"):
            order_page.click_to_header_logo_scooter()

        with allure.step("Проверить переход на главную страницу"):
            current_url = order_page.get_current_url()
            expected_url = "https://qa-scooter.praktikum-services.ru/"
            assert current_url == expected_url

    @allure.title("Открытие Дзена в новой вкладке по клику на логотип Яндекса")
    @allure.description(
        "Проверка, что при клике на логотип Яндекса открывается страница Дзена в новой вкладке"
    )
    def test_click_ya_logo_redirects_to_yandex(self):
        main_page = MainHomePage(self.driver)
        order_page = OrderPage(self.driver)

        with allure.step("Открыть главную страницу"):
            main_page.open_url(URL)

        with allure.step("Кликнуть на логотип 'Яндекса'"):
            initial_handles = order_page.get_window_handles_count()
            order_page.click_to_header_logo_yandex()
            order_page.wait_for_new_tab(initial_handles)
            order_page.switch_to_last_tab()

        with allure.step("Ожидать загрузки страницы Дзена"):
            order_page.wait_url_contains("dzen")

        with allure.step("Проверить, что открылась страница Дзена"):
            current_url = order_page.get_current_url()
            assert "dzen.ru" in current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
