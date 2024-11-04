from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGIN_BUTTON_MAIN_PAGE, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON_AUTH_PAGE, PROFILE_LINK
#Авторизация
def login(driver, email, password):
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LOGIN_BUTTON_AUTH_PAGE).click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

#Проверка отображения кнопки 'Сделать заказ' на главной
def check_order_button_displayed(driver):
    ORDER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
    assert driver.find_element(*ORDER_BUTTON).is_displayed(), "Кнопка 'Сделать заказ' не отображается после входа в систему."
driver = webdriver.Chrome()

# 1. Вход по кнопке "Войти в аккаунт" на главной
driver.get("https://stellarburgers.nomoreparties.site/")
driver.find_element(*LOGIN_BUTTON_MAIN_PAGE).click()
login(driver, "antropova15@yande.ru", "111111")
check_order_button_displayed(driver)
driver.quit()

# 2. Вход через кнопку "Личный кабинет"
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
driver.find_element(*PROFILE_LINK).click()
login(driver, "antropova15@yande.ru", "111111")
check_order_button_displayed(driver)
driver.quit()

# 3. Вход через кнопку в форме регистрации
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()
login(driver, "antropova15@yande.ru", "111111")
check_order_button_displayed(driver)
driver.quit()

# 4. Вход через форму восстановления пароля
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()
login(driver, "antropova15@yande.ru", "111111")
check_order_button_displayed(driver)
driver.quit()