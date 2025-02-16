import allure
import pytest

from Utilities.readproperties import readConfig
from pageObjects.CartPage import CartPage
from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.PaymentPage import PaymentPage
from pageObjects.ReigsterPage import RegisterPage


class Test_016_LoginBeforeCheckout:

    baseURL = readConfig.getApplicationURL()
    email = readConfig.getLoginvalidEmail()
    password = readConfig.getLoginvalidPassword()
    cardname = readConfig.getCardName()
    cardnumber = readConfig.getCardNumber()
    cardcvv = readConfig.getCVV()
    expiremonth = readConfig.getExpireMonth()
    expireyear = readConfig.getExpireYear()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_LoginBeforeCheckout(self,setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.verifyTitle()
        self.hp.clickSignupLogin()
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.rp = RegisterPage(self.driver)
        self.rp.verifyLoggedinUser()
        self.cp = CartPage(self.driver)
        self.hp = HomePage(self.driver)
        self.hp.scrolltoProduct()
        self.hp.addProductCart()
        self.hp.clickCart()
        self.cp.verifyTitle()
        self.cp.proceedCheckout()
        self.cop = CheckOutPage(self.driver)
        self.cop.verifyDeliveryAddressDetails()
        self.cop.scrollDownToPlaceOrder()
        self.cop.sendComment()
        self.cop.clickPlaceOrder()
        self.paymentpage = PaymentPage(self.driver)
        self.paymentpage.setCardName(self.cardname)
        self.paymentpage.setCardNumber(self.cardnumber)
        self.paymentpage.setCardCVV(self.cardcvv)
        self.paymentpage.setCardExpireMonth(self.expiremonth)
        self.paymentpage.setCardExpireYear(self.expireyear)
        self.paymentpage.clickPaymentPlace()
        self.paymentpage.verifySuccessfullyPlaced()
        self.hp.clickDelete()
        self.rp.verifyAccountDeleted()
        self.rp.clickContinue()

