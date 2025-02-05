from selenium import webdriver

from TestCases.conftest import setup
from pageObjects.HomePage import HomePage
from Utilities.readproperties import readConfig
from pageObjects.TestcasePage import TestCasePage


class Test_007_TestCase :

    baseURL = readConfig.getApplicationURL()

    def test_TestcaseValidate(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.verifyTitle()
        self.hp.clickTestCases()
        self.tp = TestCasePage(self.driver)
        self.tp.verifyTitle()

