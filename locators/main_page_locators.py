from selenium.webdriver.common.by import By

question_button = (By.ID, "accordion__heading-{}")
answer_text = (By.ID, "accordion__panel-{}")
cookie_button = (By.CLASS_NAME, "App_CookieButton__3cvqF")
order_button = (By.CLASS_NAME, "Button_Button__ra12g")
order_button_2 = (
    By.XPATH,
    './/button[@class = "Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]',
)
