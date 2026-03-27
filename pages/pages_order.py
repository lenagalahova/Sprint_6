import allure
from locators.order_page import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators

    @allure.step("Ввести имя")
    def set_name(self, my_name):
        self.send_keys(self.locators.name, my_name)

    @allure.step("Ввести фамилию")
    def set_surname(self, my_surname):
        self.send_keys(self.locators.surname, my_surname)

    @allure.step("Ввести адрес")
    def set_adress(self, my_adress):
        self.send_keys(self.locators.adress, my_adress)

    @allure.step("Выбрать станцию метро 'Черкизовская'")
    def set_metro(self):
        self.click(self.locators.metro)
        self.click(self.locators.metro_cherkizovskaya)

    @allure.step("Ввести телефон")
    def set_tel(self, my_tel):
        self.send_keys(self.locators.tel, my_tel)

    @allure.step("Заполнить первый шаг формы заказа: Имя, Фамилия, Адрес, Телефон")
    def fill_my_data_1_step(self, my_name, my_surname, my_adress, my_tel):
        self.set_name(my_name)
        self.set_surname(my_surname)
        self.set_adress(my_adress)
        self.set_metro()
        self.set_tel(my_tel)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.click(self.locators.next_button)

    @allure.step("Ввести дату")
    def set_data(self, my_data):
        self.send_keys(self.locators.data, my_data)

    @allure.step("Выбрать период аренды: трое суток")
    def set_rental_period(self):
        self.click(self.locators.rental_period)
        self.click(self.locators.rental_period_3)

    @allure.step("Закрыть календарь нажатием ENTER")
    def close_calendar_with_enter(self):
        super().close_calendar(self.locators.data)

    @allure.step("Заполнить второй шаг формы заказа: Дата")
    def fill_my_data_2_step(self, my_data):
        self.set_data(my_data)
        self.close_calendar_with_enter()
        self.set_rental_period()

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button_2(self):
        self.click(self.locators.order_button_2)

    @allure.step("Подтвердить заказ в модальном окне")
    def click_to_yes_button(self):
        self.wait_visible(self.locators.popup_order)
        self.click(self.locators.yes_button)

    @allure.step("Получить текст подтверждения заказа")
    def get_text_of_order(self):
        return self.get_text(self.locators.text_of_order)

    @allure.step("Кликнуть на логотип 'Самоката'")
    def click_to_header_logo_scooter(self):
        self.click(self.locators.header_logo_scooter)

    @allure.step("Кликнуть на логотип 'Яндекса'")
    def click_to_header_logo_yandex(self):
        self.click(self.locators.header_logo_yandex)
