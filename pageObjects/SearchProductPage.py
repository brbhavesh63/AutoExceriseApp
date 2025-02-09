from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


class SearchProductPage:
    div_searchedProducts_xpath = '//*[@class="features_items"]//div[@class="col-sm-4"]'
    div_addToCart_xpath = 'div/div/div[2]/div/a'
    btn_continueshopping_xpath = "//*[text()='Continue Shopping']"
    lbl_productName_xpath = 'div/div/div[2]/div/p'


    def __init__(self,driver):
        self.driver = driver
        self.products_name = []

    def addSearchedProductsToCart(self):
        listSearchedProducts = self.driver.find_elements(By.XPATH, self.div_searchedProducts_xpath)
        for product in listSearchedProducts:
            hover_product = product.find_element(By.XPATH,"div")
            action = ActionChains(self.driver)
            action.move_to_element(hover_product).perform()
            wait_addCart = WebDriverWait(self.driver,10)
            wait_addCart.until(element_to_be_clickable((By.XPATH,self.div_addToCart_xpath)))
            addCart_ele = product.find_element(By.XPATH, self.div_addToCart_xpath)
            print(addCart_ele.is_displayed())
            addCart_ele.click()
            product_txt = product.find_element(By.XPATH,self.lbl_productName_xpath).text
            self.products_name.append(product_txt)
            print(self.products_name)
            wait_modal = WebDriverWait(self.driver,10)
            wait_modal.until(visibility_of_element_located((By.XPATH,self.btn_continueshopping_xpath)))
            self.driver.find_element(By.XPATH,self.btn_continueshopping_xpath).click()