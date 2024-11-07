import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import MAIN_PAGE_URL, REGISTER_PAGE_URL, LOGIN_PAGE_URL, FORGOT_PASSWORD_PAGE_URL
from data import LOGIN_EMAIL, LOGIN_PASSWORD
from locators import LOGIN_BUTTON_MAIN_PAGE, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON_AUTH_PAGE, PROFILE_LINK, LOGIN_BUTTON, LOGIN_BUTTON_REG_PAGE

@pytest.mark.usefixtures("driver")

class TestAuthorization:
    # Авторизация
    def login(self, driver):
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(LOGIN_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)
        driver.find_element(*LOGIN_BUTTON_AUTH_PAGE).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_PAGE_URL))

    # Проверка отображения кнопки 'Сделать заказ' на главной
    def check_order_button_displayed(self, driver):
        ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))
        assert driver.find_element(*ORDER_BUTTON).is_displayed(), "Кнопка 'Оформить заказ' не отображается после входа в систему."

    # 1. Вход по кнопке "Войти в аккаунт" на главной
    def test_login_main_page_button(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*LOGIN_BUTTON_MAIN_PAGE).click()
        self.login(driver)
        self.check_order_button_displayed(driver)
        assert driver.current_url == MAIN_PAGE_URL, "Не удалось попасть на главную страницу после входа."

    # 2. Вход через кнопку "Личный кабинет"
    def test_login_profile_button(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*PROFILE_LINK).click()
        self.login(driver)
        self.check_order_button_displayed(driver)
        assert driver.current_url == MAIN_PAGE_URL, "Не удалось попасть на главную страницу после входа."

    # 3. Вход через кнопку в форме регистрации
    def test_login_registration_form(self, driver):
        driver.get(REGISTER_PAGE_URL)
        driver.find_element(*LOGIN_BUTTON_REG_PAGE).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_PAGE_URL))
        self.login(driver)
        self.check_order_button_displayed(driver)
        assert driver.current_url == MAIN_PAGE_URL, "Не удалось попасть на главную страницу после входа."

    # 4. Вход через форму восстановления пароля
    def test_login_password_recovery_form(self, driver):
        driver.get(FORGOT_PASSWORD_PAGE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_PAGE_URL))
        self.login(driver)
        self.check_order_button_displayed(driver)
        assert driver.current_url == MAIN_PAGE_URL, "Не удалось попасть на главную страницу после входа."