import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import Locators
from src.url import *


class TestBuilderSections:

    def test_move_to_sauce(self, driver):
        driver.find_element(*Locators.SAUCE).click()

        head = (
            WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located(Locators.TEXT_SAUCE))
            .text
        )
        assert head == "Соус с шипами Антарианского плоскоходца"


    def test_move_to_filling(self, driver):
        driver.find_element(*Locators.FILLING).click()

        head = (
            WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located(Locators.TEXT_FILLING))
            .text
        )
        assert head == "Начинки"


    def test_move_to_bun(self, driver):
        driver.find_element(*Locators.FILLING).click()
        driver.find_element(*Locators.BUN).click()
        
        head = (
            WebDriverWait(driver, 10)
            .until(EC.visibility_of_element_located(Locators.TEXT_BUN))
            .text
        )
        assert head == "Булки"