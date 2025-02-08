import time
from argparse import Action
from threading import activeCount

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


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
    h2_filterProductTitle_xpath = '(//h2)[3]'
    div_category_xpath = '//*[@id="accordian"]/div'
    div_allcategory_xpath = 'div/h4/a'
    div_subcategory_xpath = 'div/div/ul/li/a'
    div_fullsubcategory_xpath = '(//*[@id="accordian"]/div/div/div/ul/li/a)[4]'
    div_brands_xpath = "//*[@class='brands_products']"
    div_listbrands_xpath = "//*[@class='brands_products']/div/ul/li"


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

    def validateTitleOfFilteredProduct(self):
        h2_productTitle_ele = self.driver.find_element(By.XPATH,self.h2_filterProductTitle_xpath)
        product_title_txt = h2_productTitle_ele.text
        assert product_title_txt == 'WOMEN - DRESS PRODUCTS'

    def clickMenCategory(self):
        all_category = self.driver.find_elements(By.XPATH, self.div_category_xpath)
        for category in all_category:
            category_ele = category.find_element(By.XPATH,self.div_allcategory_xpath)
            category_txt = category_ele.text
            print(category_txt)
            if category_txt == "MEN":
                category_ele.click()
                wait = WebDriverWait(self.driver , 10)
                wait.until(visibility_of_element_located((By.XPATH,self.div_fullsubcategory_xpath)))
                subcategory_ele = category.find_element(By.XPATH, self.div_subcategory_xpath)
                subcategory_txt = subcategory_ele.text
                print(subcategory_txt)
                if subcategory_txt == 'TSHIRTS':
                    subcategory_ele.click()
                    break

    def validateSelectedFilterProductPageTitle(self):
        act_title = self.driver.title
        assert act_title == 'Automation Exercise - Tshirts Products'

    def visibleBrand(self):
        brands = self.driver.find_element(By.XPATH, self.div_brands_xpath)
        assert brands.is_displayed()

    def clickBrand(self,selectBrandName):
        listBrands = self.driver.find_elements(By.XPATH, self.div_listbrands_xpath)
        for brand in listBrands:
            select_brand = brand.find_element(By.XPATH,"a").text
            brand_name = select_brand[3:].strip()
            if brand_name == selectBrandName:
                brand.click()
                brand_act_title = self.driver.title
                converted_brandName = selectBrandName.capitalize()
                if brand_act_title == f'Automation Exercise - {converted_brandName} Products':
                    assert True
                    break