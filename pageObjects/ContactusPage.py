from itertools import dropwhile

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from Locators.locators import Locators_ContactUs

class ContactUs:

    name_xpath = Locators_ContactUs.txtbox_name_xpath
    email_xpath = Locators_ContactUs.txtbox_email_xpath
    subject_xpath = Locators_ContactUs.txtbox_subject_xpath
    message_xpath = Locators_ContactUs.txtbox_msg_xpath
    submit_xpath = Locators_ContactUs.btn_submit_xpath
    successmsg_xpath = Locators_ContactUs.lbl_successmsg_xpath

    def __init__(self,driver):
        self.driver = driver

    def setName(self,name):
        self.driver.find_element(By.XPATH, self.name_xpath).send_keys(name)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def setSubject(self,subject):
        self.driver.find_element(By.XPATH, self.subject_xpath).send_keys(subject)

    def setMessage(self,message):
        self.driver.find_element(By.XPATH, self.message_xpath).send_keys(message)

    def clickSubmit(self):
        self.driver.find_element(By.XPATH, self.submit_xpath).click()

    def acceptAlert(self):
        alert = Alert(self.driver)
        alert.accept()

    def successDisplay(self):
        success_msg = self.driver.find_element(By.XPATH, self.successmsg_xpath)
        success_msg_txt = success_msg.text
        if success_msg.is_displayed():
            assert success_msg_txt == 'Success! Your details have been submitted successfully. '
        else:
            assert False



