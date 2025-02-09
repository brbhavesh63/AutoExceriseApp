from selenium.webdriver.common.by import By
from pageObjects.ProductDetailPage import ProductDetailPage
from pageObjects.ProductPage import ProductPage
from pageObjects.SearchProductPage import SearchProductPage


class CartPage:

    lbl_subscription_xpath = '//*[@class="single-widget"]/h2'
    txtbox_email_xpath = '//*[@id="susbscribe_email"]'
    btn_subsribe_xpath = '//*[@id="subscribe"]'
    msg_success_xpath = '//*[@class="alert-success alert"]'
    tbl_cartinfo_xpath = '//*[@id="cart_info_table"]'
    tbl_cartdesc_xpath = 'td[2]/h4/a'
    tbl_qty_xpath = '//table/tbody/tr/td[4]/button'
    btn_checkout_xpath = '//*[@class="btn btn-default check_out"]'
    link_reglogin_xpath = '//*[text()="Register / Login"]'
    tbl_productdetails = '//*[@id="cart_info_table"]'
    tbl_productdetails_rows = '//*[@id="cart_info_table"]/tbody/tr'
    tbl_productdetails_columns = '//*[@id="cart_info_table"]/tbody/td'
    tbl_productdelete_xpath = '//*[@id="cart_info_table"]/tbody/tr/td[6]'
    lbl_emptycart_xpath = '//*[@id="empty_cart"]'

    def __init__(self,setup):
        self.driver = setup
        # self.cart_product_details = []
        self.pp = ProductPage(self.driver)
        self.spp = SearchProductPage(self.driver)

    def verifyTitle(self):
        act_title = self.driver.title
        assert act_title == 'Automation Exercise - Checkout'

    def scrollDowntoFooter(self):
        # subscription_txt = self.driver.find_element(By.XPATH,self.lbl_subscription_xpath)
        # self.driver.execute_script("arguments[0].scrollIntoView();", subscription_txt)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def verifySubscription(self):
        subscription_txt = self.driver.find_element(By.XPATH,self.lbl_subscription_xpath).text
        assert subscription_txt == 'SUBSCRIPTION'

    def sendEmail(self):
        self.driver.find_element(By.XPATH , self.txtbox_email_xpath).send_keys('brbhavesh@gmail.com')

    def clickSubscribe(self):
        self.driver.find_element(By.XPATH, self.btn_subsribe_xpath).click()
        successmsg = self.driver.find_element(By.XPATH, self.msg_success_xpath)
        successmsg_txt = successmsg.text
        if successmsg.is_displayed:
            assert "You have been successfully subscribed!" == successmsg_txt
        else:
            assert False

    # def verifyProductAddedToCart(self):
    #     cartinfo = self.driver.find_elements(By.XPATH,self.tbl_cartinfo_xpath)
    #     for extracttxt in cartinfo:
    #         product_name = extracttxt.find_element(By.XPATH,self.tbl_cartdesc_xpath).text

    def getQty(self):
        qty = int(self.driver.find_element(By.XPATH,self.tbl_qty_xpath).text)
        self.pdp = ProductDetailPage(self.driver)
        assert qty == self.pdp.qty

    def proceedCheckout(self):
        self.driver.find_element(By.XPATH,self.btn_checkout_xpath).click()

    def clickRegLoginLink(self):
        self.driver.find_element(By.XPATH,self.link_reglogin_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tbl_productdetails_rows))


    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tbl_productdetails_columns))

    def validateProductAddedToCart(self):
        cart_product_details = []
        for i in range(1,self.getNoOfRows()+1):
            cartTable = self.driver.find_element(By.XPATH,self.tbl_cartinfo_xpath)
            productName = cartTable.find_element(By.XPATH,f'tbody/tr[{i}]/td[2]/h4').text
            productPrice = cartTable.find_element(By.XPATH,f'tbody/tr[{i}]/td[3]/p').text
            cart_product_details.append((productName,productPrice))
            # cartProductList = cart_product_details.append[productName,productPrice]
        print(f"This is my cart information: {cart_product_details}")
        if self.pp.selected_product_details == cart_product_details:
            assert True
        else:
            assert False

    def deleteProduct(self):
        # for i in range(1,self.getNoOfRows()+1):
        #     cartTable = self.driver.find_element(By.XPATH,self.tbl_cartinfo_xpath)
        #     cartTable.find_element(By.XPATH, f'tbody/tr[1]/td[6]/a/i').click()
        noOfRows = self.driver.find_elements(By.XPATH,self.tbl_productdetails_rows)
        for row in noOfRows:
            row.find_element(By.XPATH, 'td[6]/a/i').click()

    def emptyCart(self):
        emptycarttxt = self.driver.find_element(By.XPATH, self.lbl_emptycart_xpath)
        if emptycarttxt.is_displayed():
            assert True
        else:
            assert False

    def validateSearchedProductAddedToCart(self):
        cart_product_details = []
        for i in range(1, self.getNoOfRows() + 1):
            cartTable = self.driver.find_element(By.XPATH, self.tbl_cartinfo_xpath)
            productName = cartTable.find_element(By.XPATH, f'tbody/tr[{i}]/td[2]/h4').text
            cart_product_details.append((productName))
            print(cart_product_details)
            # cartProductList = cart_product_details.append[productName,productPrice]
        print(f"This is my cart information: {cart_product_details}")
        if self.spp.products_name == cart_product_details:
            assert True
        else:
            assert False
