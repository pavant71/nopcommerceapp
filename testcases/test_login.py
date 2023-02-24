import pytest
from selenium import webdriver
from pageobjects.loginpage import loginpage
from testcases import confitest

class Test_001_login:
    BaseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"

    @pytest.fixture()
    def test_homepage(self, setup):
        self.driver = setup()
        self.driver.get(self.BaseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store.Login":
            assert True
        else:
            assert False

    @pytest.fixture()
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.lp = loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False