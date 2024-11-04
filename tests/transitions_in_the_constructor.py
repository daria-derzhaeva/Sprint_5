from locators import Locators
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
driver.find_element(*Locators.LOGIN_BUTTON_HOME_PAGE).click()
driver.find_element(*Locators.EMAIL_FIELD).send_keys("12345690@ya.ru")
driver.find_element(*Locators.PASSWORD_FIELD).send_keys("123456789")
driver.find_element(*Locators.ENTRY_BUTTON).click()

driver.find_element(*Locators.SAUCE_BUTTON).click()
sauce = driver.find_element(*Locators.SAUCE_TEXT)
assert sauce.text == "Соусы", "Ошибка при выходе в раздел Соусы"

driver.find_element(*Locators.BUNS_BUTTON).click()
buns = driver.find_element(*Locators.BUNS_TEXT)
assert buns.text == "Булки", "Ошибка при выходе в раздел Булки"

driver.find_element(*Locators.FILLINGS_BUTTON).click()
fillings = driver.find_element(*Locators.FILLINGS_TEXT)
assert fillings.text == "Начинки", "Ошибка при выходе в раздел Начинки"
driver.quit()