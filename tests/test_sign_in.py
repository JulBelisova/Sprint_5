import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.data import Credentials
from src.locators import Locators
from src.url import *


class TestSignIn:

    def test_sign_in_from_main_site(self, driver):
        email = Credentials.email
        password = Credentials.password

        driver.find_element(*Locators.BUTTON_SIGN_IN_MAIN).click()
        driver.find_element(*Locators.ENTER_EMAIL).send_keys(email)
        driver.find_element(*Locators.ENTER_PASSWORD).send_keys(password)

        driver.find_element(*Locators.ENTER_BUTTON).click()
        reg_text = (
            WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located(Locators.ORDER))
            .text
        )

        assert reg_text == "Оформить заказ"

    def test_sign_in_from_my_account_button(self, driver):
        email = Credentials.email
        password = Credentials.password
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((Locators.BUTTON_MY_ACCOUNT))
        )
        driver.find_element(*Locators.BUTTON_MY_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((Locators.ENTER_EMAIL))
        )
        driver.find_element(*Locators.ENTER_EMAIL).send_keys(email)
        driver.find_element(*Locators.ENTER_PASSWORD).send_keys(password)

        driver.find_element(*Locators.ENTER_BUTTON).click()
        reg_text = (
            WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located(Locators.ORDER))
            .text
        )

        assert reg_text == "Оформить заказ"

    def test_sign_in_from_retistration(self, driver):
        email = Credentials.email
        password = Credentials.password

        driver.get(sign_up_site)
        driver.find_element(*Locators.BUTTON_SIGN_IN_FROM_REGISTRATION).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((Locators.ENTER_EMAIL))
        )

        driver.find_element(*Locators.ENTER_EMAIL).send_keys(email)
        driver.find_element(*Locators.ENTER_PASSWORD).send_keys(password)

        driver.find_element(*Locators.ENTER_BUTTON).click()
        reg_text = (
            WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located(Locators.ORDER))
            .text
        )

        assert reg_text == "Оформить заказ"

    def test_sign_in_from_recovery_password(self, driver):
        email = Credentials.email
        password = Credentials.password

        driver.get(forgot_password)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.BUTTON_SIGN_IN_FROM_PASSWORD_RECOVERY)
        )
        button.click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((Locators.ENTER_EMAIL))
        )

        driver.find_element(*Locators.ENTER_EMAIL).send_keys(email)
        driver.find_element(*Locators.ENTER_PASSWORD).send_keys(password)

        driver.find_element(*Locators.ENTER_BUTTON).click()
        reg_text = (
            WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located(Locators.ORDER))
            .text
        )

        assert reg_text == "Оформить заказ"
