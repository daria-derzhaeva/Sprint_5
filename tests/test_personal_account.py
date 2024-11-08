import pytest
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import TEST_EMAIL, TEST_PASSWORD

class TestEntryPersonalAccount:
    def test_entry_personal_account(self, driver):
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(TEST_PASSWORD)
        driver.find_element(*Locators.ENTRY_BUTTON).click()
        driver.find_element(*Locators.LK_BUTTON).click()
        profile = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.PROFILE_TEXT))
        assert profile.text == "Профиль", "Ошибка при переходе в лк клиента"