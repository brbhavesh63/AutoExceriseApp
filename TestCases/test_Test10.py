import allure
import pytest

from Utilities.readproperties import readConfig
from pageObjects.HomePage import HomePage


class Test_09_Subscribe:
    baseURL = readConfig.getApplicationURL()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.MINOR)
    def test_subscribe(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.verifyTitle()
        self.hp.scrollDowntoFooter()
        self.hp.verifySubscription()
        self.hp.sendEmail()
        self.hp.clickSubscribe()