import pytest
from selenium import webdriver

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from Utilities.readproperties import readConfig

class Test_002_ValidLogin:
    baseURL = readConfig.getApplicationURL()
    email = readConfig.getLoginvalidEmail()
    password = readConfig.getLoginvalidPassword()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_validLogin(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.verifyTitle()
        self.hp.clickSignupLogin()
        self.lp = LoginPage(self.driver)
        self.lp.verifyLogintxtdisplayed()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()




