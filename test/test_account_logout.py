import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import MAIN_PAGE_URL, PROFILE_PAGE_URL, LOGIN_PAGE_URL
from data import LOGIN_EMAIL, LOGIN_PASSWORD
from locators import LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON_AUTH_PAGE, PROFILE_LINK, LOGOUT_BUTTON

@pytest.mark.usefixtures("driver")
class TestLogout:
    def test_logout(self, driver):
        driver.get(LOGIN_PAGE_URL)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(LOGIN_BUTTON_AUTH_PAGE)).click()

        # Авторизация
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(LOGIN_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)
        driver.find_element(*LOGIN_BUTTON_AUTH_PAGE).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_PAGE_URL))

        # Переход в профиль
        driver.find_element(*PROFILE_LINK).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_PAGE_URL))

        # Разлогин
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGOUT_BUTTON))
        driver.find_element(*LOGOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_to_be(LOGIN_PAGE_URL))
        assert driver.current_url == LOGIN_PAGE_URL, "Не удалось выйти из аккаунта."