from Utilities.readproperties import readConfig
from pageObjects.CartPage import CartPage
from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage
from pageObjects.SearchProductPage import SearchProductPage


class Test_009_SearchProduct:

    baseURL = readConfig.getApplicationURL()

    def test_Search(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.verifyTitle()
        self.hp.clickProducts()
        self.pp = ProductPage(self.driver)
        self.pp.verifyTitle()
        self.pp.searchProducts()
        self.pp.visibleSearchProductslbl()
        self.pp.visibleSearchedProductsNames()
        self.spp = SearchProductPage(self.driver)
        self.hp.scrolltoProduct()
        self.spp.addSearchedProductsToCart()
        self.hp.clickCart()
        self.cp = CartPage(self.driver)
        self.cp.validateSearchedProductAddedToCart()
