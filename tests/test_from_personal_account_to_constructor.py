import pytest
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import TEST_EMAIL, TEST_PASSWORD

class TestPersonalAccount:
    def test_from_personal_account(self, driver):
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(TEST_PASSWORD)
        driver.find_element(*Locators.ENTRY_BUTTON).click()
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        burger = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.BURGER_TEXT))
        assert burger.text == "Соберите бургер", "Ошибка при переходе из лк в конструктор по кнопке Конструктор"

    def test_from_account_Stellar_burgers(self, driver):
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(TEST_PASSWORD)
        driver.find_element(*Locators.ENTRY_BUTTON).click()
        driver.find_element(*Locators.LK_BUTTON).click()
        driver.find_element(*Locators.STELLAR_BURGERS_TEXT).click()
        burger = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.BURGER_TEXT))
        assert burger.text == "Соберите бургер", "Ошибка при переходе из лк в конструктор по кнопке Stellar burgers"