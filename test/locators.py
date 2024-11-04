from selenium.webdriver.common.by import By

# Локаторы для прохождения регистрации
NAME_INPUT = (By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20' ]//fieldset[1]//input")  # Поле для ввода имени
EMAIL_INPUT = (By.XPATH, "//form/fieldset[2]/div/div/input")  # Поле для ввода email
PASSWORD_INPUT = (By.XPATH, "//form/fieldset[3]/div/div/input")  # Поле для ввода пароля
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации
ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")  # Сообщение об ошибке при некорректном пароле

# Локаторы для авторизации
LOGIN_PASSWORD_INPUT = (By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20' ]//fieldset[2]//input")  # Поле для ввода пароля
LOGIN_EMAIL_INPUT = (By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20' ]//fieldset[1]//input")  # Поле для ввода email
LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button") # Локатор для кнопки "Войти в аккаунт" на главной странице
LOGIN_BUTTON_AUTH_PAGE = (By.XPATH, "//*[@id='root']/div/main/div/form/button") # Локатор для кнопки "Войти" на странице авторизации
PROFILE_LINK = (By.XPATH, "//*[@id='root']/div/header/nav/a") # Локатор для кнопки "Войти в аккаунт" на главной странице
ORDER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button') # Локатор для кнопки 'Сделать заказ'
# Локаторы для перехода в конструктор
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") # Локатор для кнопки "Конструктор"
LOGO = (By.XPATH, "//*[@id='root']/div/header/nav/div")  # Локатор для логотипа
CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']") # Локатор для заголовка в констуркторе
LOGOUT_BUTTON = (By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button[text()='Выход']") # Локатор для кнопки Выйти

# Локаторы для перехода в по разделам
CONSTRUCTOR_BUNS_SECTION = (By.XPATH, "//section[@class = 'BurgerIngredients_ingredients__1N8v2']/div/div[1]") # Локатор для раздела Булки
CONSTRUCTOR_SAUCES_SECTION = (By.XPATH, "//section[@class = 'BurgerIngredients_ingredients__1N8v2']/div/div[2]") # Локатор для раздела Соусы
CONSTRUCTOR_FILLINGS_SECTION = (By.XPATH, "//section[@class = 'BurgerIngredients_ingredients__1N8v2']/div/div[3]") # Локатор для раздела Начинки
