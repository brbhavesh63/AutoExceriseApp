import time

import pytest

from TestCases.conftest import setup
from Utilities.readproperties import readConfig
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage


class Test_004_Logout:
    baseURL = readConfig.getApplicationURL()
    email = readConfig.getLoginvalidEmail()
    password = readConfig.getPassword()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logout(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.clickSignupLogin()
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.hp.clickLogout()
        self.lp.verifyLogintxtdisplayed()


