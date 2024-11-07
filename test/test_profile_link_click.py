import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON_AUTH_PAGE, PROFILE_LINK
from urls import MAIN_PAGE_URL, LOGIN_PAGE_URL, PROFILE_PAGE_URL
from data import LOGIN_EMAIL, LOGIN_PASSWORD

@pytest.mark.usefixtures("driver")

class TestLinkClik:
    def test_profile_link_click(self, driver):
        # Авторизация
        driver.get(LOGIN_PAGE_URL)
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(LOGIN_EMAIL)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)
        driver.find_element(*LOGIN_BUTTON_AUTH_PAGE).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_PAGE_URL))

        # Переход в личный кабинет
        driver.find_element(*PROFILE_LINK).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_PAGE_URL))

        # Проверяем, что мы на странице личного кабинета
        assert driver.current_url == PROFILE_PAGE_URL, "Не удалось перейти в личный кабинет."