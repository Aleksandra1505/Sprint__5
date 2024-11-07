import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON_MAIN_PAGE, LOGIN_BUTTON_AUTH_PAGE, PROFILE_LINK, CONSTRUCTOR_BUTTON, LOGO, CONSTRUCTOR_HEADER
from urls import MAIN_PAGE_URL, LOGIN_PAGE_URL
from data import LOGIN_EMAIL, LOGIN_PASSWORD

@pytest.mark.usefixtures("driver")

class TestNavigationFromProfile:
    # Авторизация
    def login(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*LOGIN_BUTTON_MAIN_PAGE).click()
        driver.get(LOGIN_PAGE_URL)
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(LOGIN_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)
        driver.find_element(*LOGIN_BUTTON_AUTH_PAGE).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_PAGE_URL))

    # 1. Проверка перехода в конструктор через кнопку Конструктор
    def test_navigate_to_constructor_button(self, driver):
        self.login(driver)
        driver.find_element(*PROFILE_LINK).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CONSTRUCTOR_BUTTON)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CONSTRUCTOR_HEADER))
        assert driver.current_url == MAIN_PAGE_URL, "Мы не на странице конструктора!"

    # 2. Проверка перехода в конструктор через логотип
    def test_navigate_to_constructor_logo(self, driver):
        self.login(driver)
        driver.find_element(*PROFILE_LINK).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGO)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(CONSTRUCTOR_HEADER))
        assert driver.current_url == MAIN_PAGE_URL, "Мы не на странице конструктора!"