import sys
import os
import time

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import Locators
from src.url import *


class TestBuilderSections:

    def test_move_to_sauce(self, driver):
        driver.find_element(*Locators.SAUCE).click()

        time.sleep(3)
        assert driver.find_element(*Locators.SAUCE_CHECK).is_displayed()

    def test_move_to_filling(self, driver):
        driver.find_element(*Locators.FILLING).click()
        time.sleep(3)
        assert driver.find_element(*Locators.FILLING_CHECK).is_displayed()

    def test_move_to_bun(self, driver):
        driver.find_element(*Locators.FILLING).click()
        driver.find_element(*Locators.BUN).click()

        time.sleep(3)
        assert driver.find_element(*Locators.BUN_CHECK).is_displayed()
