import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import MAIN_PAGE_URL
from locators import CONSTRUCTOR_SAUCES_SECTION, CONSTRUCTOR_FILLINGS_SECTION, HEADER_BUNS_SECTION, HEADER_SAUCES_SECTION, HEADER_FILLINGS_SECTION, SELECT_TAB_CONSTRUCTOR

@pytest.mark.usefixtures("driver")

class TestIngredientsNavigations:
    # 1. проверка перехода к разделу Начинки
    def test_navigation_to_fillings(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*CONSTRUCTOR_FILLINGS_SECTION).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(HEADER_FILLINGS_SECTION))
        assert driver.find_element(*SELECT_TAB_CONSTRUCTOR).text == driver.find_element(*HEADER_FILLINGS_SECTION).text

    # 2. проверка перехода к разделу Булки
    def test_navigation_to_buns(self, driver):
        driver.get(MAIN_PAGE_URL)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(HEADER_BUNS_SECTION))
        assert driver.find_element(*SELECT_TAB_CONSTRUCTOR).text == driver.find_element(*HEADER_BUNS_SECTION).text

    # 3. проверка перехода к разделу Соусы
    def test_navigation_to_sauces(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*CONSTRUCTOR_SAUCES_SECTION).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(HEADER_SAUCES_SECTION))
        assert driver.find_element(*SELECT_TAB_CONSTRUCTOR).text == driver.find_element(*HEADER_SAUCES_SECTION).text