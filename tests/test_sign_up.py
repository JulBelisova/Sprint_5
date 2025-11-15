import sys
import os

# Добавляем корень проекта в Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.data import Credentials
from src.helper import generate_registration_data
from src.locators import Locators
from src.url import *


class TestRegistrationWithNewCredentials:

    def test_sucsess_registration(self, driver):
        # arrange
        driver.get(sign_up_site)
        email, password = generate_registration_data()
        name = "Петя"
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        # act
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        reg_text = (
            WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located(Locators.TEXT_ENTER))
            .text
        )
        # assert
        assert reg_text == "Вход"
        assert driver.current_url == main_site + "login"


class TestCheckingIncorrectPassword:

    def test_failed_registration_incorrect_password(self, driver):
        # arrange
        driver.get(sign_up_site)
        email = generate_registration_data()
        password = '12'
        name = "Петя"
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        # act
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        reg_text = (
            WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located(Locators.INCORRECT_PASSWORD))
            .text
        )
        # assert
        assert reg_text == "Некорректный пароль"
        assert driver.current_url == main_site + "register"