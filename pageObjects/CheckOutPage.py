from selenium.webdriver.common.by import By

from Utilities.readproperties import readConfig
from pageObjects.CartPage import CartPage


class CheckOutPage:
    addressdetails_xpath = '//*[@id="address_delivery"]/li'
    placeOrder_xpath = "//*[text()='Place Order']"
    comment_xpath = '//*[@name="message"]'


    def __init__(self,driver):
        self.driver = driver
        self.cp = CartPage(self.driver)
        firstname = readConfig.getFirstName()
        lastname = readConfig.getLastName()
        city = readConfig.getCity()
        address = readConfig.getAddress()
        zipcode = readConfig.getZipcode()
        mobile = readConfig.getMobile()
        state = readConfig.getState()
        fullname = firstname+" "+lastname
        citystatezip = city+" "+state+" "+zipcode
        self.addressdetailsRegister = [fullname,address,citystatezip,mobile]
        print(self.addressdetailsRegister)



    def getNoOfLines(self):
        return len(self.driver.find_elements(By.XPATH,self.addressdetails_xpath))


    def verifyDeliveryAddressDetails(self):
        address_detailsList = []
        for i in range(1,self.getNoOfLines()+1):
            if i%2==0:
                addressDetails = self.driver.find_element(By.XPATH,f'//*[@id="address_delivery"]/li[{i}]').text
                print(addressDetails)
                if addressDetails.startswith("Mr. "):
                    addressDetails = addressDetails[4:]
                address_detailsList.append(addressDetails)
        print(address_detailsList)
        assert self.addressdetailsRegister == address_detailsList

    def scrollDownToPlaceOrder(self):
      ScrollDownPlaceOrder = self.driver.find_element(By.XPATH,self.placeOrder_xpath)
      self.driver.execute_script("arguments[0].scrollIntoView();", ScrollDownPlaceOrder)

    def sendComment(self):
        self.driver.find_element(By.XPATH,self.comment_xpath).send_keys('Nice Experience')

    def clickPlaceOrder(self):
        self.driver.find_element(By.XPATH,self.placeOrder_xpath).click()



    

