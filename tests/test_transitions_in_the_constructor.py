import pytest
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTransitions:
    def test_navigate_to_sauce(self, driver):
        driver.find_element(*Locators.SAUCE_BUTTON).click()
        sauce = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.SAUCE_TEXT))
        assert sauce.text == "Соусы", "Ошибка при переходе в раздел Соусы"

    def test_navigate_to_buns(self, driver):
        driver.find_element(*Locators.SAUCE_BUTTON).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()
        buns = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.BUNS_TEXT))
        assert buns.text == "Булки", "Ошибка при переходе в раздел Булки"

    def test_navigate_to_fillings(self, driver):
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        fillings = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.FILLINGS_TEXT))
        assert fillings.text == "Начинки", "Ошибка при переходе в раздел Начинки"




