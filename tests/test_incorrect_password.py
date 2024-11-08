import pytest
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import TEST_EMAIL, TEST_INCORRECT_PASSWORD, TEST_NAME

class TestIncorrectPassword:
    def test_incorrect_password(self, driver):
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_AT_THE_ENTRANCE_BUTTON).click()
        driver.find_element(*Locators.NAME_FIELD).send_keys(TEST_NAME)
        driver.find_element(*Locators.EMAIL_FIELD_REGISTRATION).send_keys(TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(TEST_INCORRECT_PASSWORD)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        password = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.INCORRECT_PASSWORD_TEXT))
        assert password.text == "Некорректный пароль", "Вход осуществляется с невалидным паролем"