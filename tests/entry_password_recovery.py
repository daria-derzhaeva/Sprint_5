from locators import Locators
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(*Locators.LK_BUTTON).click()
driver.find_element(*Locators.RECOVER_PASSWORD_BUTTON).click()
driver.find_element(*Locators.ENTRY_RECOVER_PASSWORD_BUTTON).click()
driver.find_element(*Locators.EMAIL_FIELD).send_keys("12345690@ya.ru")
driver.find_element(*Locators.PASSWORD_FIELD).send_keys("123456789")
driver.find_element(*Locators.ENTRY_BUTTON).click()
driver.quit()


