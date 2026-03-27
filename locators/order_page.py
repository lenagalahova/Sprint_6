from selenium.webdriver.common.by import By

title = (By.CLASS_NAME, "Order_Header__BZXOb")
name = (By.XPATH, './/input[@placeholder = "* Имя"]')
surname = (By.XPATH, './/input[@placeholder = "* Фамилия"]')
adress = (By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]')
metro = (By.XPATH, './/input[@placeholder = "* Станция метро"]')
metro_cherkizovskaya = (
    By.XPATH,
    './/div[@class = "Order_Text__2broi" and text()="Черкизовская"]',
)
tel = (By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]')
next_button = (By.XPATH, ".//button[text()='Далее']")
data = (By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]')
rental_period = (By.CLASS_NAME, "Dropdown-control")
rental_period_3 = (By.XPATH, './/div[text()="трое суток"]')
order_button_2 = (
    By.XPATH,
    './/button[@class = "Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]',
)
popup_order = (By.XPATH, './/div[text()="Хотите оформить заказ?"]')
yes_button = (
    By.XPATH,
    './/button[@class = "Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]',
)
text_of_order = (
    By.XPATH,
    './/div[@class = "Order_ModalHeader__3FDaJ" and text() = "Заказ оформлен"]',
)
header_logo_scooter = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
header_logo_yandex = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
