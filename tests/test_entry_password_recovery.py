import pytest
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import TEST_EMAIL, TEST_PASSWORD

class TestLogin:
    def test_password_recovery(self, driver):
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.RECOVER_PASSWORD_BUTTON).click()
        driver.find_element(*Locators.ENTRY_RECOVER_PASSWORD_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(TEST_PASSWORD)
        driver.find_element(*Locators.ENTRY_BUTTON).click()

        burger_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.BURGER_TEXT))
        assert burger_element.text == "Соберите бургер", "Текст элемента не соответствует ожидаемому"



