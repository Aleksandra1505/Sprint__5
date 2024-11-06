from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import CONSTRUCTOR_BUNS_SECTION, CONSTRUCTOR_SAUCES_SECTION, CONSTRUCTOR_FILLINGS_SECTION, HEADER_BUNS_SECTION, HEADER_SAUCES_SECTION, HEADER_FILLINGS_SECTION, SELECT_TAB_CONSTRUCTOR
import time

# 1. проверка перехода к разделу Начинки
def test_navigation_to_fillings():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*CONSTRUCTOR_FILLINGS_SECTION).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Начинки']")))

    assert driver.find_element(*SELECT_TAB_CONSTRUCTOR).text == driver.find_element(*HEADER_FILLINGS_SECTION).text

    time.sleep(2)
    driver.quit()

# 2. проверка перехода к разделу Булки
def test_navigation_to_buns():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Булки']")))

    assert driver.find_element(*SELECT_TAB_CONSTRUCTOR).text == driver.find_element(*HEADER_BUNS_SECTION).text

    time.sleep(2)
    driver.quit()

# 3. проверка перехода к разделу Соусы
def test_navigation_to_sauces():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*CONSTRUCTOR_SAUCES_SECTION).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Соусы']")))

    assert driver.find_element(*SELECT_TAB_CONSTRUCTOR).text == driver.find_element(*HEADER_SAUCES_SECTION).text

    time.sleep(2)
    driver.quit()

test_navigation_to_sauces()
test_navigation_to_fillings()
test_navigation_to_buns()