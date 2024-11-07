import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import NAME_INPUT, EMAIL_INPUT, PASSWORD_INPUT, REGISTER_BUTTON, ERROR_MESSAGE
from urls import REGISTER_PAGE_URL, LOGIN_PAGE_URL
from helpers import generate_email

@pytest.mark.usefixtures("driver")

class TestRegistration:
    #Успешная регистрация
    def test_successful_registration(self, driver):
        driver.get(REGISTER_PAGE_URL)
        driver.find_element(*NAME_INPUT).send_keys("Саша")
        # Генерация email
        generated_email = generate_email()
        driver.find_element(*EMAIL_INPUT).send_keys(generated_email)
        driver.find_element(*PASSWORD_INPUT).send_keys("111111")
        driver.find_element(*REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_PAGE_URL))
        assert driver.current_url == LOGIN_PAGE_URL, "Юзер не зарегистрирован, URL не совпадает."

    #Проваленная регистрация
    def test_failed_registration(self, driver):
        driver.get(REGISTER_PAGE_URL)
        driver.find_element(*NAME_INPUT).send_keys("Саша")
        # Генерация email
        generated_email = generate_email()
        driver.find_element(*EMAIL_INPUT).send_keys(generated_email)
        driver.find_element(*PASSWORD_INPUT).send_keys("11") #Вводим неверный пароль
        driver.find_element(*REGISTER_BUTTON).click()
        error_message = driver.find_element(*ERROR_MESSAGE)
        assert error_message.is_displayed(), "Ошибка: сообщение об ошибке не отображается."
        assert error_message.text == "Некорректный пароль", "Ошибка: текст сообщения не совпадает"
