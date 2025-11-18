import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.data import Credentials
from src.locators import Locators
from src.url import *


class TestLogOut:

    def test_log_out(self, driver):
        email = Credentials.email
        password = Credentials.password

        driver.find_element(*Locators.BUTTON_SIGN_IN_MAIN).click()
        driver.find_element(*Locators.ENTER_EMAIL).send_keys(email)
        driver.find_element(*Locators.ENTER_PASSWORD).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        driver.find_element(*Locators.BUTTON_MY_ACCOUNT).click()
        log_out_button = (
            WebDriverWait(driver, 10)
            .until(EC.element_to_be_clickable(Locators.LOG_OUT))
        )
        log_out_button.click()

        reg_text = (
            WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located(Locators.TEXT_ENTER))
            .text
        )
     
        assert reg_text == "Вход"
        assert driver.current_url == main_site + "login"