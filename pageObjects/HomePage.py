import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageObjects.ProductPage import ProductPage


class HomePage:

    btn_signuplogin_xpath = "//*[text()=' Signup / Login']"
    btn_logout_xpath = "//*[text()=' Logout']"
    btn_contactus_xpath = "//*[text()=' Contact us']"
    btn_testcase_xpath = "//*[text()=' Test Cases']"
    btn_product_xpath = "//*[text()=' Products']"
    lbl_subscription_xpath = '//*[@class="single-widget"]/h2'
    txtbox_email_xpath = '//*[@id="susbscribe_email"]'
    btn_subsribe_xpath = '//*[@id="subscribe"]'
    msg_success_xpath = '//*[@class="alert-success alert"]'
    btn_cart_xpath = "//*[text()=' Cart']"
    productname_xpath = 'p'
    imgwrap_product_xpath = "//*[@class='product-image-wrapper']"
    overlay_product_xpath = '//*[@class="overlay-content"]'
    btn_continue_xpath = "//*[text()='Continue Shopping']"
    productprice_xpath = 'h2'
    btn_scrollup_id = 'scrollUp'
    btn_delete_xpath = "//*[text()=' Delete Account']"



    def __init__(self,driver):
        self.driver = driver
        self.selected_product_details=[]
        self.pp = ProductPage(self.driver)

    def verifyTitle(self):
        acttitle = self.driver.title
        assert acttitle == 'Automation Exercise'

    def clickSignupLogin(self):
        self.driver.find_element(By.XPATH,self.btn_signuplogin_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH , self.btn_logout_xpath).click()

    def clickContactUs(self):
        self.driver.find_element(By.XPATH, self.btn_contactus_xpath).click()

    def clickTestCases(self):
        self.driver.find_element(By.XPATH, self.btn_testcase_xpath).click()

    def clickProducts(self):
        self.driver.find_element(By.XPATH, self.btn_product_xpath).click()

    def scrollDowntoFooter(self):
        # subscription_txt = self.driver.find_element(By.XPATH,self.lbl_subscription_xpath)
        # self.driver.execute_script("arguments[0].scrollIntoView();", subscription_txt)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def verifySubscription(self):
        subscription_txt = self.driver.find_element(By.XPATH, self.lbl_subscription_xpath).text
        assert subscription_txt == 'SUBSCRIPTION'

    def sendEmail(self):
        self.driver.find_element(By.XPATH, self.txtbox_email_xpath).send_keys('brbhavesh@gmail.com')

    def clickSubscribe(self):
        self.driver.find_element(By.XPATH, self.btn_subsribe_xpath).click()
        successmsg = self.driver.find_element(By.XPATH, self.msg_success_xpath)
        successmsg_txt = successmsg.text
        if successmsg.is_displayed:
            assert "You have been successfully subscribed!" == successmsg_txt
        else:
            assert False

    def clickCart(self):
        self.driver.find_element(By.XPATH, self.btn_cart_xpath).click()

    def clickProductItem(self):
        imgwrappers = self.driver.find_elements(By.XPATH, self.imgwrap_product_xpath)
        for imgwrapper in imgwrappers:
            imgwrapper.find_element(By.XPATH,'div[2]').click()
            break

    def scrolltoProduct(self):
        self.pp.scrollDowntoProduct()

    def addProductCart(self):
        total_items = self.driver.find_elements(By.XPATH, self.overlay_product_xpath)
        i = 1
        for item in total_items:
            if i <= 2:
                hover_item = item.find_element(By.XPATH, "a")
                action = ActionChains(self.driver)
                action.move_to_element(item).perform()
                product_price = item.find_element(By.XPATH, self.productprice_xpath).text
                product_name = item.find_element(By.XPATH, self.productname_xpath).text
                self.selected_product_details.append((product_name, product_price))
                hover_item.click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()
                i = i + 1
            else:
                break
        print(self.selected_product_details)

    def scrollUp(self):
        self.pp.scrollUp()

    def clickDelete(self):
        self.driver.find_element(By.XPATH, self.btn_delete_xpath).click()






