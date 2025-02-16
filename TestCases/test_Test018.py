import allure
import pytest

from TestCases.conftest import setup
from Utilities.readproperties import readConfig
from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage


class Test018_ViewCategoryProducts:

    baseURL = readConfig.getApplicationURL()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ViewCategoryProducts(self,setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.verifyTitle()
        self.hp.validateCategoryVisible()
        self.hp.scrolltoProduct()
        self.hp.clickWomenCategory()
        self.pp = ProductPage(self.driver)
        self.pp.validateTitleOfFilteredProduct()
        self.pp.clickMenCategory()
        self.pp.validateSelectedFilterProductPageTitle()
