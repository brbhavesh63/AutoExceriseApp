from Utilities.readproperties import readConfig
from pageObjects.CartPage import CartPage
from pageObjects.HomePage import HomePage
from pageObjects.ProductDetailPage import ProductDetailPage
from pageObjects.ProductPage import ProductPage


class Test_012_addtocart:

    baseURL = readConfig.getApplicationURL()

    def test_AddtoCart(self,setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.verifyTitle()
        self.hp.clickProducts()
        self.pp = ProductPage(self.driver)
        self.pp.scrollDowntoProduct()
        self.pp.addProductToCart()
        self.pdp = ProductDetailPage(self.driver)
        self.pdp.clickviewCart()
        self.cp = CartPage(self.driver)
        self.cp.validateProductAddedToCart()
