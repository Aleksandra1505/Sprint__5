from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGIN_BUTTON_MAIN_PAGE, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON_AUTH_PAGE, PROFILE_LINK

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Авторизация
driver.find_element(*LOGIN_BUTTON_MAIN_PAGE).click()
WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("antropova15@yande.ru")
driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("111111")
driver.find_element(*LOGIN_BUTTON_AUTH_PAGE).click()
WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

# Переход в личный кабинет
driver.find_element(*PROFILE_LINK).click()
WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))

# Проверяем, что мы на странице личного кабинета
assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile", "Не удалось перейти в личный кабинет."

driver.quit()