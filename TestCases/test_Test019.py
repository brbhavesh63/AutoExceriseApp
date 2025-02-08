from TestCases.conftest import setup
from Utilities.readproperties import readConfig
from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage


class Test019_ViewBrandProducts:

    baseURL = readConfig.getApplicationURL()

    def test_ViewBrandProducts(self,setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.clickProducts()
        self.pp = ProductPage(self.driver)
        self.pp.visibleBrand()
        self.pp.scrollDowntoProduct()
        self.pp.clickBrand('MADAME')
        self.pp.clickBrand('BABYHUG')


