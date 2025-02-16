import pytest

from Utilities.readproperties import readConfig
from pageObjects.HomePage import HomePage
from pageObjects.ContactusPage import ContactUs
import time

class Test_006_Contactus:

    baseURL = readConfig.getApplicationURL()
    name = readConfig.getContactName()
    email = readConfig.getContactEmail()
    subject = readConfig.getSubject()
    message = readConfig.getMessage()

    @pytest.mark.regression
    def test_contactForm(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.verifyTitle()
        self.hp.clickContactUs()
        self.cp = ContactUs(self.driver)
        self.cp.setName(self.name)
        self.cp.setEmail(self.email)
        self.cp.setSubject(self.subject)
        self.cp.setMessage(self.message)
        self.cp.clickSubmit()
        self.cp.acceptAlert()
        time.sleep(2)
        self.cp.successDisplay()
