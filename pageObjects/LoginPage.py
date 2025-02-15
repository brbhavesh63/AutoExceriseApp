from selenium.webdriver.common.by import By


class LoginPage:
    lbl_logintxt_xpath = '(//h2)[1]'
    txtbox_email_xpath = '//*[@data-qa="login-email"]'
    txtbox_password_xpath = '//*[@data-qa="login-password"]'
    btn_login_xpath = '//*[@data-qa="login-button"]'

    def __init__(self,driver):
        self.driver = driver

    def verifyLogintxtdisplayed(self):
        logininfo = self.driver.find_element(By.XPATH, self.lbl_logintxt_xpath)
        logininfotxt = logininfo.text
        if logininfo.is_displayed():
            assert logininfotxt == 'Login to your account'
        else:
            assert False


    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtbox_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtbox_email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()