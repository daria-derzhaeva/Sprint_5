from locators import Locators
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(*Locators.LK_BUTTON).click()
driver.find_element(*Locators.REGISTRATION_AT_THE_ENTRANCE_BUTTON).click()
driver.find_element(*Locators.NAME_FIELD).send_keys("Тестовый аккаунт yandex two")
driver.find_element(*Locators.EMAIL_FIELD_REGISTRATION).send_keys("3741020@ya.ru")
driver.find_element(*Locators.PASSWORD_FIELD).send_keys("750138AL1")
driver.find_element(*Locators.REGISTRATION_BUTTON).click()

entry_button = driver.find_element(*Locators.ENTRY_TEXT_AFTER_REGISTRATION )
assert entry_button.text == "Войти", "Текст кнопки не соответствует ожидаемому значению 'Войти'"
driver.quit()