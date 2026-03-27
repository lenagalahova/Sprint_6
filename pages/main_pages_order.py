from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from locators.order_page import (
    name,
    surname,
    adress,
    tel,
    metro,
    next_button,
    rental_period,
    rental_period_3,
    data,
    order_button_2,
    text_of_order,
    popup_order,
    yes_button,
    metro_cherkizovskaya,
    header_logo_scooter,
    header_logo_yandex,
)


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.name = name
        self.surname = surname
        self.adress = adress
        self.tel = tel
        self.metro = metro
        self.next_button = next_button
        self.rental_period = rental_period
        self.rental_period_3 = rental_period_3
        self.data = data
        self.order_button_2 = order_button_2
        self.popup_order = popup_order
        self.yes_button = yes_button
        self.text_of_order = text_of_order
        self.metro_cherkizovskaya = metro_cherkizovskaya
        self.header_logo_scooter = header_logo_scooter
        self.header_logo_yandex = header_logo_yandex

    def set_name(self, my_name):
        self.driver.find_element(*self.name).send_keys(my_name)

    def set_surname(self, my_surname):
        self.driver.find_element(*self.surname).send_keys(my_surname)

    def set_adress(self, my_adress):
        self.driver.find_element(*self.adress).send_keys(my_adress)

    def set_metro(self):
        self.driver.find_element(*self.metro).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.metro_cherkizovskaya)
        )
        self.driver.find_element(*self.metro_cherkizovskaya).click()

    def set_tel(self, my_tel):
        self.driver.find_element(*self.tel).send_keys(my_tel)

    def fill_my_data_1_step(self, my_name, my_surname, my_adress, my_tel):
        self.set_name(my_name)
        self.set_surname(my_surname)
        self.set_adress(my_adress)
        self.set_metro()
        self.set_tel(my_tel)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def set_data(self, my_data):
        self.driver.find_element(*self.data).send_keys(my_data)
        self.driver.find_element(*self.data).send_keys(Keys.ENTER)

    def set_rental_period(self):
        self.driver.find_element(*self.rental_period).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.rental_period_3)
        )
        self.driver.find_element(*self.rental_period_3).click()

    def fill_my_data_2_step(self, my_data):
        self.set_data(my_data)
        self.set_rental_period()

    def click_order_button_2(self):
        self.driver.find_element(*self.order_button_2).click()

    def wait_popup_order(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.popup_order)
        )

    def click_to_yes_button(self):
        self.driver.find_element(*self.yes_button).click()

    def wait_text_of_order(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.text_of_order)
        )

    def get_text_of_order(self):
        text_order = self.driver.find_element(*self.text_of_order)
        return text_order.text


    def click_to_header_logo_scooter(self):
        self.driver.find_element(*self.header_logo_scooter).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/")
        )

    def click_to_header_logo_yandex(self):
        self.driver.find_element(*self.header_logo_yandex).click()
