import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from src.url import *
from src.data import Credentials
from src.locators import Locators

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    service = Service()
    browser = webdriver.Chrome(options=options, service=service)
    browser.get(main_site)
    yield browser
    browser.quit()
