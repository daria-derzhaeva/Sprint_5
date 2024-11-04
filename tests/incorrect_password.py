from locators import Locators
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(*Locators.LK_BUTTON).click()
driver.find_element(*Locators.REGISTRATION_AT_THE_ENTRANCE_BUTTON).click()
driver.find_element(*Locators.NAME_FIELD).send_keys("Тестовый аккаунт two")
driver.find_element(*Locators.EMAIL_FIELD_REGISTRATION).send_keys("12310@ya.ru")
driver.find_element(*Locators.PASSWORD_FIELD).send_keys("123")
driver.find_element(*Locators.REGISTRATION_BUTTON).click()
password = driver.find_element(*Locators.INCORRECT_PASSWORD_TEXT)
assert password.text == "Некорректный пароль", "Вход осуществляется с невалидным паролем"
driver.quit()