from selenium import webdriver
import pytest

@pytest.fixture()
def setup(driver):
    driver = webdriver.Chrome(executable_path="D:\\drivers\\chromedriver\\chromedriver_win32\\chromedriver.exe")
    return driver