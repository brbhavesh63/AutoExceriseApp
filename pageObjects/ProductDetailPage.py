from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProductDetailPage:

    lbl_productname_xpath = '//*[@class="product-information"]/h2'
    lbl_productdetails_xpath = '//*[@class="product-information"]/p'
    lbl_productsprice_xpath = '//*[@class="product-information"]/span/span'
    lbl_availablity_xpath = '//*[@class="product-information"]/p[2]'
    lbl_condition_xpath = '//*[@class="product-information"]/p[3]'
    lbl_brand_xpath = '//*[@class="product-information"]/p[4]'
    txt_qty_id = 'quantity'
    link_viewcart_xpath = '//*[text()="View Cart"]'
    modal_cart_xpath = '//*[@class="modal-content"]'
    btn_addcart_xpath = '//*[@class="btn btn-default cart"]'
    txt_reviewname_id = 'name'
    txt_reviewemail_id = 'email'
    txt_reviewdesc_id = 'review'
    btn_submit_id = 'button-review'
    txt_success_xpath = "//*[text()='Thank you for your review.']"


    def __init__(self,driver):
        self.driver = driver
        self.qty = 4

    def verifyTitle(self):
        act_title = self.driver.title
        if act_title == 'Automation Exercise - Product Details':
            assert True
        else:
            assert False

    def visiblityProductsDetails(self):
        productname = self.driver.find_element(By.XPATH,self.lbl_productname_xpath)
        if productname.is_displayed():
            assert True
        else:
            assert False

        productdetails = self.driver.find_element(By.XPATH, self.lbl_productdetails_xpath)
        if productdetails.is_displayed():
            assert True
        else:
            assert False

        productsprice = self.driver.find_element(By.XPATH, self.lbl_productsprice_xpath)
        if productsprice.is_displayed():
            assert True
        else:
            assert False

        availability = self.driver.find_element(By.XPATH, self.lbl_availablity_xpath)
        if availability.is_displayed():
            assert True
        else:
            assert False

        condition = self.driver.find_element(By.XPATH, self.lbl_condition_xpath)
        if condition.is_displayed():
            assert True
        else:
            assert False

        brand = self.driver.find_element(By.XPATH, self.lbl_brand_xpath)
        if brand.is_displayed():
            assert True
        else:
            assert False

    def addProductQty(self):

        self.driver.find_element(By.ID, self.txt_qty_id).clear()
        qty = self.driver.find_element(By.ID,self.txt_qty_id)
        qty.send_keys(self.qty)

    def addToCart(self):
        self.driver.find_element(By.XPATH, self.btn_addcart_xpath).click()

    def clickviewCart(self):
        wait = WebDriverWait(self.driver ,8)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.modal_cart_xpath)))
        self.driver.find_element(By.XPATH,self.link_viewcart_xpath).click()

    def sendReview(self,reviewname,reviewemail,reviewdesc):
        self.driver.find_element(By.ID, self.txt_reviewname_id).send_keys(reviewname)
        self.driver.find_element(By.ID,self.txt_reviewemail_id).send_keys(reviewemail)
        self.driver.find_element(By.ID,self.txt_reviewdesc_id).send_keys(reviewdesc)
        self.driver.find_element(By.ID,self.btn_submit_id).click()

    def verifySuccessReview(self):
        success_msg = self.driver.find_element(By.XPATH,self.txt_success_xpath).text
        if success_msg == 'Thank you for your review.':
            assert True
        else:
            assert False

    # def verifyProductDetailsAdded(self):
    #     productname = self.driver.find_element(By.XPATH,self.lbl_productname_xpath).text
    #     productdetails = self.driver.find_element(By.XPATH, self.lbl_productdetails_xpath)
    #     productsprice = self.driver.find_element(By.XPATH, self.lbl_productsprice_xpath)
    #     availability = self.driver.find_element(By.XPATH, self.lbl_availablity_xpath)
    #     condition = self.driver.find_element(By.XPATH, self.lbl_condition_xpath)
    #     brand = self.driver.find_element(By.XPATH, self.lbl_brand_xpath)
    #
    #     productdetails= {
    #         "pname" : productname,
    #         "pprice" : productsprice,
    #         "pdetails" : productdetails,
    #         "availability" : availability,
    #         "condition" : condition,
    #         "brand" : brand
    #     }
    #     return productdetails