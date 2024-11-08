import pytest
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import TEST_EMAIL, TEST_PASSWORD

class TestExit:
    def test_exit(self, driver):
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(TEST_PASSWORD)
        driver.find_element(*Locators.ENTRY_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.LK_BUTTON))
        driver.find_element(*Locators.LK_BUTTON).click()
        exit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.EXIT_BUTTON))
        exit_button.click()

        entry = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ENTRY_TEXT))
        assert entry.text == "Вход", "Ошибка при выходе из аккаунта"
