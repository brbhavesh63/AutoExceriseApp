import time

from Utilities.readproperties import readConfig
from pageObjects.CartPage import CartPage
from pageObjects.HomePage import HomePage


class Test017_RemoveProducts:
    baseURL = readConfig.getApplicationURL()

    def test_RemoveProducts(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.verifyTitle()
        self.hp.scrolltoProduct()
        self.hp.addProductCart()
        self.hp.clickCart()
        self.cp = CartPage(self.driver)
        self.cp.verifyTitle()
        self.cp.deleteProduct()
        time.sleep(2)
        self.cp.emptyCart()
