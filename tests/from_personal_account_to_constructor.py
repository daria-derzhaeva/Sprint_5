from locators import Locators
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(*Locators.LK_BUTTON).click()
driver.find_element(*Locators.EMAIL_FIELD).send_keys("12345690@ya.ru")
driver.find_element(*Locators.PASSWORD_FIELD).send_keys("123456789")
driver.find_element(*Locators.ENTRY_BUTTON).click()
driver.find_element(*Locators.LK_BUTTON).click()
driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

burger = driver.find_element(*Locators.BURGER_TEXT)
assert burger.text == "Соберите бургер", "Ошибка при переходе из лк в конструктор по кнопке Конструктор"
driver.find_element(*Locators.LK_BUTTON).click()
driver.find_element(*Locators.STELLAR_BURGERS_TEXT).click()
burger = driver.find_element(*Locators.BURGER_TEXT)
assert burger.text == "Соберите бургер", "Ошибка при переходе из лк в конструктор по кнопке Stellar burgers"
driver.quit()