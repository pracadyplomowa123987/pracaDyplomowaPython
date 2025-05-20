import pytest
from selenium import webdriver
import os
from pytest_html import extras

@pytest.fixture(scope="session", autouse=True)
def ensure_folders_exist():
    os.makedirs("../Podyplomowe/reports", exist_ok=True)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
