import allure
import pytest

from Utilities.readproperties import readConfig
from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage


class Test_009_SearchProduct:

    baseURL = readConfig.getApplicationURL()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
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


