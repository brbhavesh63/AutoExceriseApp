from selenium.webdriver.common.by import By

from Utilities.readproperties import readConfig


class PaymentPage:

    cardname_xpath = '//*[@name="name_on_card"]'
    cardnumber_xpath = '//*[@name="card_number"]'
    cardcvv_xpath = '//*[@name="cvc"]'
    cardexpiremonth_xpath = '//*[@name="expiry_month"]'
    cardexpireyear_xpath = '//*[@name="expiry_year"]'
    paymentbtn_xpath = '//*[@data-qa="pay-button"]'
    successmsg_xpath = '//*[@class="alert-success alert"]'


    def __init__(self,driver):
        self.driver = driver

    def setCardName(self,cardname):
        self.driver.find_element(By.XPATH,self.cardname_xpath).send_keys(cardname)

    def setCardNumber(self,cardnumber):
        self.driver.find_element(By.XPATH,self.cardnumber_xpath).send_keys(cardnumber)

    def setCardCVV(self,cvv):
        self.driver.find_element(By.XPATH,self.cardcvv_xpath).send_keys(cvv)

    def setCardExpireMonth(self,expiremonth):
        self.driver.find_element(By.XPATH,self.cardexpiremonth_xpath).send_keys(expiremonth)

    def setCardExpireYear(self,expireyear):
        self.driver.find_element(By.XPATH, self.cardexpireyear_xpath).send_keys(expireyear)

    def clickPaymentPlace(self):
        self.driver.find_element(By.XPATH,self.paymentbtn_xpath).click()

    def verifySuccessfullyPlaced(self):
        successmsg = self.driver.find_element(By.XPATH, self.successmsg_xpath).text
        assert successmsg in 'Your order has been placed successfully!'