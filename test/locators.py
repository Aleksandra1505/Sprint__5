from selenium.webdriver.common.by import By

# Локаторы для прохождения регистрации
NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле для ввода имени - изменено
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле для ввода email - изменено
PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле для ввода пароля - изменено
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации
ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")  # Сообщение об ошибке при некорректном пароле

# Локаторы для авторизации
LOGIN_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле для ввода пароля - изменено
LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле для ввода email - изменено
LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']") # Локатор для кнопки "Войти в аккаунт" на главной странице - изменено
LOGIN_BUTTON_AUTH_PAGE = (By.XPATH, "//a[@href='/register' and text()='Войти']") # Локатор для кнопки "Войти" на странице регистрации - изменено
PROFILE_LINK = (By.XPATH, "//p[text()='Личный Кабинет']") # Локатор для кнопки "Войти в аккаунт" через личный кабинет - изменено
ORDER_BUTTON = (By.XPATH, "//button[text()='Сделать заказ']") # Локатор для кнопки 'Сделать заказ' - изменено

# Локаторы для перехода в конструктор
CONSTRUCTOR_BUTTON = (By.CLASS_NAME, "AppHeader_header__linkText__3q_va") # Локатор для кнопки "Конструктор" - изменено
LOGO = (By.XPATH, "//a[@href='/']")  # Локатор для логотипа - изменено
CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']") # Локатор для заголовка в констуркторе
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") # Локатор для кнопки Выйти - изменено

# Локаторы для перехода в по разделам
CONSTRUCTOR_BUNS_SECTION = (By.XPATH, "//span[text()='Булки']") # Локатор для раздела Булки - изменено
CONSTRUCTOR_SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']") # Локатор для раздела Соусы - изменено
CONSTRUCTOR_FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']") # Локатор для раздела Начинки - изменено
