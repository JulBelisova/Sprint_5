import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.data import Credentials
from src.locators import Locators
from src.url import *


class TestClickBuilder:

    def test_from_my_account_to_builder(self, driver):
        email = Credentials.email
        password = Credentials.password

        driver.find_element(*Locators.BUTTON_SIGN_IN_MAIN).click()
        driver.find_element(*Locators.ENTER_EMAIL).send_keys(email)
        driver.find_element(*Locators.ENTER_PASSWORD).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER)
        )
        driver.find_element(*Locators.BUTTON_MY_ACCOUNT).click()
        button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.BUILDER)
        )
        button.click()

        reg_text = (
            WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located(Locators.BUILD_BURGER))
            .text
        )

        assert reg_text == "Соберите бургер"
        assert driver.current_url == main_site


class TestClickLogo:

    def test_from_my_account_to_logo(self, driver):
        email = Credentials.email
        password = Credentials.password
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((Locators.BUTTON_MY_ACCOUNT)))
        driver.find_element(*Locators.BUTTON_SIGN_IN_MAIN).click()
        driver.find_element(*Locators.ENTER_EMAIL).send_keys(email)
        driver.find_element(*Locators.ENTER_PASSWORD).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ORDER)
        )
        driver.find_element(*Locators.BUTTON_MY_ACCOUNT).click()

        button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGO)
        )
        button.click()

        reg_text = (
            WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located(Locators.BUILD_BURGER))
            .text
        )

        assert reg_text == "Соберите бургер"
        assert driver.current_url == main_site