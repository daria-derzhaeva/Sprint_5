import pytest
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_unique_email, generate_password, generate_name

class TestRegistration:
    def test_registration(self, driver):
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_AT_THE_ENTRANCE_BUTTON).click()
        driver.find_element(*Locators.NAME_FIELD).send_keys(generate_name())
        driver.find_element(*Locators.EMAIL_FIELD_REGISTRATION).send_keys(generate_unique_email())
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(generate_password())
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        registration_complete = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ENTRY_TEXT_AFTER_REGISTRATION))
        assert registration_complete.text == "Войти", "Текст кнопки не соответствует ожидаемому значению 'Войти'"
