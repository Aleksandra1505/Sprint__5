from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON_MAIN_PAGE, LOGIN_BUTTON_AUTH_PAGE, PROFILE_LINK, CONSTRUCTOR_BUTTON, LOGO, CONSTRUCTOR_HEADER
import time

# Функция для вызова драйвера и авторизации
def login():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*LOGIN_BUTTON_MAIN_PAGE).click()
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("antropova15@yande.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("111111")
    driver.find_element(*LOGIN_BUTTON_AUTH_PAGE).click()
    return driver

# 1. Проверка перехода в конструктор через кнопку Конструктор
def test_navigate_to_constructor_button():
    driver = login()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*PROFILE_LINK).click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CONSTRUCTOR_BUTTON)).click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CONSTRUCTOR_HEADER))
    assert driver.find_element(*CONSTRUCTOR_HEADER).is_displayed(), "Заголовок конструктора не отображается."
    driver.quit()


# 2. Проверка перехода в конструктор через логотип
def test_navigate_to_constructor_logo():
    driver = login()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*PROFILE_LINK).click()
    time.sleep(2)
    logo = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGO))
    logo.click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CONSTRUCTOR_HEADER))
    assert driver.find_element(*CONSTRUCTOR_HEADER).is_displayed(), "Заголовок конструктора не отображается."
    driver.quit()

test_navigate_to_constructor_button()
test_navigate_to_constructor_logo()