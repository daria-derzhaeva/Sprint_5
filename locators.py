from selenium.webdriver.common.by import By

class Locators:
    # Кнопка «Войти в аккаунт» на главной странице
    LOGIN_BUTTON_HOME_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Поле для ввода email
    EMAIL_FIELD = (By.XPATH, "//input[@type='text' and @name='name']")
    # Поле для ввода пароля
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password' and @name='Пароль']")
    # Поле для ввода имени
    NAME_FIELD = (By.XPATH, "//input[@type='text' and @name='name']")
    # Кнопка «Войти» при входе в лк
    ENTRY_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Кнопка «Личный кабинет»
    LK_BUTTON = (By.XPATH, "//a[@href='/account']")
    # Кнопка "Восстановить пароль"
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//a[@href='/forgot-password']")
    #Кнопка "Войти" при восстановлении пароля
    ENTRY_RECOVER_PASSWORD_BUTTON = (By.XPATH, "//a[@href='/login']")
    # Кнопка "Зарегистрироваться" при входе
    REGISTRATION_AT_THE_ENTRANCE_BUTTON = (By.XPATH, "//a[@href='/register']")
    # Кнопка "Выход" в ЛК
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    # Надпись "Вход" при авторизации
    ENTRY_TEXT = (By.XPATH, "//h2[text()='Вход']")
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    # Надпись "Соберите бургер" в конструкторе
    BURGER_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']")
    # Надпись "Stellar burgers"
    STELLAR_BURGERS_TEXT = (By.XPATH, "(//a[@href='/'])[2]")
    # Надпись "Некорректный пароль" в валидации
    INCORRECT_PASSWORD_TEXT = (By.XPATH, "//p[text()='Некорректный пароль']")
    # Кнопка "Зарегистрироваться" при регистрации
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Надпись "Профиль" в ЛК
    PROFILE_TEXT = (By.XPATH, "//a[@href='/account/profile']")
    # Надпись "Войти" после регистрации
    ENTRY_TEXT_AFTER_REGISTRATION = (By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")
    # Поле для ввода email при регистрации
    EMAIL_FIELD_REGISTRATION = (By.XPATH, "(//input[@type='text' and @name='name'])[2]")
    # Кнопка "Соусы" в конструкторе
    SAUCE_BUTTON = (By.XPATH, "//div[span[text()='Соусы']]")
    # Текст "Соусы" на странице с конструктором
    SAUCE_TEXT = (By.XPATH, "//h2[text()='Соусы']")
    # Кнопка "Булки" в конструкторе
    BUNS_BUTTON = (By.XPATH, "//div[span[text()='Булки']]")
    # Текст "Булки" в конструкторе
    BUNS_TEXT = (By.XPATH, "//h2[text()='Булки']")
    # Кнопка "Начинки" в конструкторе
    FILLINGS_BUTTON = (By.XPATH, "//div[span[text()='Начинки']]")
    # Текст "Начинки" в конструкторе
    FILLINGS_TEXT = (By.XPATH, "//h2[text()='Начинки']")