import time

from TestCases import test_Test01
from Utilities.readproperties import readConfig
from pageObjects.CartPage import CartPage
from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from pageObjects.PaymentPage import PaymentPage
from pageObjects.ReigsterPage import RegisterPage


class Test_014_RegisterWhileCheckout:

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
    cardname = readConfig.getCardName()
    cardnumber = readConfig.getCardNumber()
    cardcvv = readConfig.getCVV()
    expiremonth = readConfig.getExpireMonth()
    expireyear = readConfig.getExpireYear()

    def test_RegisterWhileCheckout(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.verifyTitle()
        self.hp.scrolltoProduct()
        self.hp.addProductCart()
        self.hp.scrollUp()
        time.sleep(2)
        self.hp.clickCart()
        self.cp = CartPage(self.driver)
        self.cp.verifyTitle()
        self.cp.proceedCheckout()
        self.cp.clickRegLoginLink()
        self.rp = RegisterPage(self.driver)
        self.rp.setName(self.name)
        self.rp.setEmail(self.email)
        self.rp.clickSignup()
        self.rp.accountInfoDisplayed()
        self.rp.clickRadio()
        self.rp.setPassword(self.password)
        self.rp.setBirthdate(self.day, self.month, self.year)
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
        self.hp.clickCart()
        self.cp.proceedCheckout()
        self.cop = CheckOutPage(self.driver)
        self.cop.verifyDeliveryAddressDetails()
        self.cop.scrollDownToPlaceOrder()
        self.cop.sendComment()
        self.cop.clickPlaceOrder()
        self.payementpage = PaymentPage(self.driver)
        self.payementpage.setCardName(self.cardname)
        self.payementpage.setCardNumber(self.cardnumber)
        self.payementpage.setCardCVV(self.cardcvv)
        self.payementpage.setCardExpireMonth(self.expiremonth)
        self.payementpage.setCardExpireYear(self.expireyear)
        self.payementpage.clickPaymentPlace()
        self.payementpage.verifySuccessfullyPlaced()
        self.rp.clickContinue()
        self.hp.clickDelete()
        self.rp.verifyAccountDeleted()
        self.rp.clickContinue()




