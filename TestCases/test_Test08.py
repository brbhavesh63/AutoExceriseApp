import allure
import pytest

from TestCases.conftest import setup
from Utilities.readproperties import readConfig
from pageObjects.HomePage import HomePage
from pageObjects.ProductDetailPage import ProductDetailPage
from pageObjects.ProductPage import ProductPage


class Test_008_Products:

    baseURL = readConfig.getApplicationURL()

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_products(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.verifyTitle()
        self.hp.clickProducts()
        self.pp = ProductPage(self.driver)
        self.pp.verifyTitle()
        self.pp.ProductsListVisible()
        self.pp.scrollDowntoProduct()
        self.pp.clickFirstProducts()
        self.pdp = ProductDetailPage(self.driver)
        self.pdp.verifyTitle()
        self.pdp.visiblityProductsDetails()