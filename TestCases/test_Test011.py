import allure
import pytest

from pageObjects.CartPage import CartPage
from pageObjects.HomePage import HomePage
from Utilities.readproperties import readConfig


class Test_011_Cart:
    baseURL = readConfig.getApplicationURL()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.MINOR)
    def test_subscribecart(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.clickCart()
        self.cp = CartPage(self.driver)
        self.cp.scrollDowntoFooter()
        self.cp.sendEmail()
        self.cp.clickSubscribe()
        self.cp.verifySubscription()