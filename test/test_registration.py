import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import NAME_INPUT, EMAIL_INPUT, PASSWORD_INPUT, REGISTER_BUTTON, ERROR_MESSAGE
from helpers import generate_email

#Успешная регистрация
def test_successful_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*NAME_INPUT).send_keys("Саша")
    time.sleep(2)

    # Генерация email
    generated_email = generate_email()
    driver.find_element(*EMAIL_INPUT).send_keys(generated_email)
    time.sleep(2)

    driver.find_element(*PASSWORD_INPUT).send_keys("111111")
    time.sleep(2)

    driver.find_element(*REGISTER_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be("https://stellarburgers.nomoreparties.site/login"))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', "Юзер не зарегистрирован, URL не совпадает."

    driver.quit()

#Проваленная регистрация
def test_failed_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*NAME_INPUT).send_keys("Саша")
    time.sleep(2)

    # Генерация email
    generated_email = generate_email()
    driver.find_element(*EMAIL_INPUT).send_keys(generated_email)
    time.sleep(2)

    driver.find_element(*PASSWORD_INPUT).send_keys("11") #Вводим неверный пароль
    time.sleep(2)

    driver.find_element(*REGISTER_BUTTON).click()
    time.sleep(2)

    error_message = driver.find_element(*ERROR_MESSAGE)
    assert error_message.is_displayed(), "Ошибка: сообщение об ошибке не отображается."
    assert error_message.text == "Некорректный пароль", "Ошибка: текст сообщения не совпадает"

    driver.quit()

test_successful_registration()
test_failed_registration()