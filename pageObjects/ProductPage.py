import time
from argparse import Action
from threading import activeCount

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ProductPage:
    imgwrapper_products_xpath = "//*[@class='product-image-wrapper']"
    wrqpper_products_xpath = '//*[@class="features_items"]'
    btn_viewdetails_xpath = "div[2]"
    wrapper_singleproduct_xpath = '(//*[@class ="single-products"])[3]'
    search_products_xpath = '//*[@id="search_product"]'
    lbl_searchproducts_xpath = '(//h2)[3]'
    wrapper_productinfo_xpath = '//*[@class="productinfo text-center"]'
    productname_xpath = 'p'
    btn_search_id = 'submit_search'
    overlay_product_xpath = '//*[@class="overlay-content"]'
    btn_continue_xpath = "//*[text()='Continue Shopping']"
    productprice_xpath = 'h2'
    btn_scrollup_id = 'scrollUp'



    def __init__(self,driver):
        self.driver = driver
        self.selected_product_details=[]

    def verifyTitle(self):
        act_title = self.driver.title
        if act_title == 'Automation Exercise - All Products':
            assert True
        else:
            assert False

    def ProductsListVisible(self):
        products_wrapper = self.driver.find_element(By.XPATH,self.wrqpper_products_xpath)
        assert products_wrapper.is_displayed()

    def scrollDowntoProduct(self):
        wrapper_singleproduct = self.driver.find_element(By.XPATH,self.wrapper_singleproduct_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", wrapper_singleproduct)

    def clickFirstProducts(self):
        products_imgwrapper = self.driver.find_elements(By.XPATH,self.imgwrapper_products_xpath)
        for product_wrapper in products_imgwrapper:
            product_wrapper.find_element(By.XPATH, self.btn_viewdetails_xpath).click()
            break

    def searchProducts(self):
        self.driver.find_element(By.XPATH,self.search_products_xpath).send_keys('Blue')
        self.driver.find_element(By.ID,self.btn_search_id).click()

    def visibleSearchProductslbl(self):
        searchedproductlbl = self.driver.find_element(By.XPATH,self.lbl_searchproducts_xpath)
        if searchedproductlbl.is_displayed():
            assert True
        else:
            assert False

    def visibleSearchedProductsNames(self):
        product_info = self.driver.find_elements(By.XPATH, self.wrapper_productinfo_xpath)
        productsname = []
        for products_name in product_info:
            product_name = products_name.find_element(By.XPATH, self.productname_xpath).text
            print(product_name)
            productsname.append(product_name)
        for searched_text in productsname:
            assert 'Blue' or 'BLUE' in searched_text


    def addProductToCart(self):
        total_items = self.driver.find_elements(By.XPATH,self.overlay_product_xpath)
        i = 1
        for item in total_items:
            if i<=2:
                hover_item = item.find_element(By.XPATH, "a")
                action = ActionChains(self.driver)
                action.move_to_element(item).perform()
                product_price = item.find_element(By.XPATH, self.productprice_xpath).text
                product_name = item.find_element(By.XPATH, self.productname_xpath).text
                self.selected_product_details.append((product_name,product_price))
                hover_item.click()
                time.sleep(2)
                if i == 1:
                    self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()
                i = i +1
            else:
                break
        print(self.selected_product_details)
                ####### BELOW SOMEWHAT CLOSE #####
                # for i in range(1, len(total_items)):
                #     for item in total_items:
                #         hover_item = item.find_element(By.XPATH, f"a[@data-product-id='{i}']")
                #         action = ActionChains(self.driver)
                #         action.move_to_element(item).perform()
                #         hover_item.click()
                #         time.sleep(2)
                #         self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()
                #
                # total_items = self.driver.find_elements(By.XPATH, self.overlay_product_xpath)

                # # Outer loop for iterating through total_items
                # for i in range(1, min(len(total_items), 3)):  # Limit i to 2 as per original logic
                #     for item in total_items:
                #         hover_item = item.find_element(By.XPATH, f"a[@data-product-id='{i}']")
                #
                #         action = ActionChains(self.driver)
                #         action.move_to_element(item).perform()
                #         hover_item.click()
                #         time.sleep(2)
                #
                #         self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()
                #         break  # Exit inner loop after the first matching item
    def scrollUp(self):
        self.driver.find_element(By.ID, self.btn_scrollup_id).click()


