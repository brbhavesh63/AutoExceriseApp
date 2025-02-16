import allure
import pytest
from selenium import webdriver
from pageObjects.ReigsterPage import RegisterPage
from pageObjects.HomePage import HomePage
from Utilities.readproperties import readConfig


@allure.severity(allure.severity_level.NORMAL)
class Test_001_Signup:

    baseURL = readConfig.getApplicationURL()
    name = readConfig.getName()
    email = readConfig.getSignupEmail()
    password = readConfig.getPassword()
    day = readConfig.getDay()
    month = readConfig.getMonth()
    year = readConfig.getYear()
    firstname = readConfig.getFirstName()
    lastname = readConfig.getLastName()
    company = readConfig.getCompany()
    city = readConfig.getCity()
    address = readConfig.getAddress()
    zipcode = readConfig.getZipcode()
    mobile = readConfig.getMobile()
    state = readConfig.getState()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_signup(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.verifyTitle()
        self.hp.clickSignupLogin()
        self.rp = RegisterPage(self.driver)
        self.rp.signupDisplayed()
        self.rp.setName(self.name)
        self.rp.setEmail(self.email)
        self.rp.clickSignup()
        self.rp.accountInfoDisplayed()
        self.rp.clickRadio()
        self.rp.setPassword(self.password)
        self.rp.setBirthdate(self.day,self.month,self.year)
        self.rp.clickCheckbnox()
        self.rp.setFirstName(self.firstname)
        self.rp.setLastName(self.lastname)
        self.rp.setAddress(self.address)
        self.rp.setState(self.state)
        self.rp.setCity(self.city)
        self.rp.setZipcode(self.zipcode)
        self.rp.setMobile(self.mobile)
        self.rp.clickCreateAccount()
        self.rp.checkAccountCreatedtxtvisibile()
        self.rp.clickContinue()
        self.rp.verifyLoggedinUser()
        self.rp.clickDeleteAccount()
        self.rp.verifyAccountDeleted()

    # def test_VerifyTitle(self,setup):
    #     self.driver = setup
    #     self.driver.maximize_window()
    #     self.driver.get(self.baseURL)
    #     self.rp = Register(self.driver)
    #     self.rp.verifyTitle()
    #     self.driver.close()