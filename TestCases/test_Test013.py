from TestCases.conftest import setup
from Utilities.readproperties import readConfig
from pageObjects.CartPage import CartPage
from pageObjects.HomePage import HomePage
from pageObjects.ProductDetailPage import ProductDetailPage


class Test_013_ProductQty:

    baseURL = readConfig.getApplicationURL()

    def test_ProductQty(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.verifyTitle()
        self.hp.clickProductItem()
        self.pdp = ProductDetailPage(self.driver)
        self.pdp.verifyTitle()
        self.pdp.addProductQty()
        self.pdp.addToCart()
        self.pdp.clickviewCart()
        self.cp = CartPage(self.driver)
        self.cp.getQty()
        # self.cp = CartPage(self.driver)
        # self.cp.clickviewCart()

