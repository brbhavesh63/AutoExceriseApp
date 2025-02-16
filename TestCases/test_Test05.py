import allure
import pytest

from Utilities.readproperties import readConfig
from pageObjects.HomePage import HomePage
from pageObjects.ReigsterPage import RegisterPage



class Test_005_AlreadyUser:

    baseURL = readConfig.getApplicationURL()
    name = readConfig.getName()
    email = readConfig.getLoginvalidEmail()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.MINOR)
    def test_existinguser(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.verifyTitle()
        self.hp.clickSignupLogin()
        self.rp = RegisterPage(self.driver)
        self.rp.setName(self.name)
        self.rp.setEmail(self.email)
        self.rp.clickSignup()
        self.rp.verifySignupMsg()

