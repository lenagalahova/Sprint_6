import pytest
from selenium import webdriver
from data import URL


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()
