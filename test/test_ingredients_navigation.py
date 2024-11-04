from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import CONSTRUCTOR_BUNS_SECTION, CONSTRUCTOR_SAUCES_SECTION, CONSTRUCTOR_FILLINGS_SECTION
import time

#Проверка перехода к заданному разделу
def check_section_navigation(driver, section_locator):
    driver.find_element(*section_locator).click()

# 1. проверка перехода к разделу Начинки
def test_navigation_to_fillings():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    check_section_navigation(driver, CONSTRUCTOR_FILLINGS_SECTION)
    time.sleep(2)
    driver.quit()

# 2. проверка перехода к разделу Булки
def test_navigation_to_buns():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    check_section_navigation(driver, CONSTRUCTOR_FILLINGS_SECTION)
    time.sleep(4)
    check_section_navigation(driver, CONSTRUCTOR_BUNS_SECTION)
    time.sleep(2)
    driver.quit()

# 3. проверка перехода к разделу Соусы
def test_navigation_to_sauces():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    check_section_navigation(driver, CONSTRUCTOR_SAUCES_SECTION)
    time.sleep(2)
    driver.quit()

test_navigation_to_sauces()
test_navigation_to_fillings()
test_navigation_to_buns()