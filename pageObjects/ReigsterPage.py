from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Utilities.readproperties import readConfig
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class RegisterPage :
    fname = readConfig.getFirstName()
    txtbox_name_xpath = '//*[@data-qa="signup-name"]'
    txtbox_email_xpath = '//*[@data-qa="signup-email"]'
    btn_signup_xpath = '//*[@data-qa="signup-button"]'
    lbl_signup_xpath = '(//h2)[3]'
    lbl_accountinfo_xpath = '(//b)[1]'

    rdo_gender_id = 'id_gender1'
    txtbox_password_xpath = '//*[@data-qa="password"]'
    select_day_xpath = '//*[@data-qa="days"]'
    select_month_xpath = '//*[@data-qa="months"]'
    select_year_xpath = '//*[@data-qa="years"]'
    check_newsltr_xpath = '//*[@id="newsletter"]'
    check_optin_xpath = '//*[@id="optin"]'
    txtbox_fname_xpath = '//*[@data-qa="first_name"]'
    txtbox_lname_xpath = '//*[@data-qa="last_name"]'
    txtbox_cmpnyname_xpath = '//*[@data-qa="company"]'
    txtbox_address_xpath = '//*[@data-qa="address"]'
    txtbox_state_xpath = '//*[@data-qa="state"]'
    txtbox_city_xpath = '//*[@data-qa="city"]'
    txtbox_zip_xpath = '//*[@data-qa="zipcode"]'
    txtbox_mobile_xpath = '//*[@data-qa="mobile_number"]'
    btn_createac_xpath = '//*[@data-qa="create-account"]'
    lbl_usersignuptxt_xpath = '//*[text()="New User Signup!"]'
    lbl_accinfo_xpath = '(//b)[1]'
    lbl_accountcreated_xpath ='//b'
    btn_continue_xpath = '//*[@data-qa="continue-button"]'
    btn_loggedinuser_xpath = '//*[text()=" Logged in as "]'
    btn_deleteaccount_xpath = '//a[text()=" Delete Account"]'
    lbl_deleteaccounttxt_xpath = '//b'
    lbl_signupmsg_xpath = '//*[@action="/signup"]/p'
    btn_createacc_xpath = '//*[@data-qa="create-account"]'

    def __init__(self,driver):
        self.driver = driver

    def signupDisplayed(self):
        # act_title = self.driver.title
        # exp_title = 'Automation Exercise - Signup / Login'
        # assert act_title == exp_title
        signupInfo = self.driver.find_element(By.XPATH,self.lbl_signup_xpath)
        if signupInfo.is_displayed():
            assert True
        else:
            assert False

    def accountInfoDisplayed(self):
        accountinfo = self.driver.find_element(By.XPATH, self.lbl_accountinfo_xpath)
        accountinfo_txt = accountinfo.text
        if accountinfo.is_displayed():
            assert accountinfo_txt == 'ENTER ACCOUNT INFORMATION'
        else:
            print('Account Information not displayed')
            assert False

    def setName(self,name):
        self.driver.find_element(By.XPATH, self.txtbox_name_xpath).send_keys(name)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtbox_email_xpath).send_keys(email)

    def clickSignup(self):
        self.driver.find_element(By.XPATH,self.btn_signup_xpath).click()

    def clickRadio(self):
        self.driver.find_element(By.ID,self.rdo_gender_id).click()

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtbox_password_xpath).send_keys(password)

    # Select DropDown -> Selecting Birthdate of the user
    def setBirthdate(self,date,month,year):
        dateddown = Select(self.driver.find_element(By.XPATH,self.select_day_xpath))
        dateddown.select_by_value(date)

        monthddown = Select(self.driver.find_element(By.XPATH,self.select_month_xpath))
        monthddown.select_by_value(month)

        yearddown = Select(self.driver.find_element(By.XPATH,self.select_year_xpath))
        yearddown.select_by_value(year)

    # Select checkbox of news letter & special offers
    def clickCheckbnox(self):
        newsletter = self.driver.find_element(By.XPATH, self.check_newsltr_xpath)
        wait = WebDriverWait(self.driver , timeout=2)
        wait.until(lambda d : newsletter.is_displayed())
        newsletter.click()
        self.driver.find_element(By.XPATH,self.check_optin_xpath).click()

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txtbox_fname_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txtbox_lname_xpath).send_keys(lname)

    def setCompanyName(self,cname):
        self.driver.find_element(By.XPATH,self.txtbox_cmpnyname_xpath).send_keys(cname)

    def setAddress(self,address):
        self.driver.find_element(By.XPATH, self.txtbox_address_xpath).send_keys(address)

    def setCity(self,city):
        self.driver.find_element(By.XPATH, self.txtbox_city_xpath).send_keys(city)

    def setState(self,state):
        self.driver.find_element(By.XPATH, self.txtbox_state_xpath).send_keys(state)

    def setZipcode(self,zip):
        self.driver.find_element(By.XPATH, self.txtbox_zip_xpath).send_keys(zip)

    def setMobile(self,mobile):
        self.driver.find_element(By.XPATH, self.txtbox_mobile_xpath).send_keys(mobile)

    def clickCreateAccount(self):
        self.driver.find_element(By.XPATH, self.btn_createacc_xpath).click()

    def checkAccountCreatedtxtvisibile(self):
        accountcreated = self.driver.find_element(By.XPATH, self.lbl_accountcreated_xpath)
        accountcreatedtxt = accountcreated.text
        print(accountcreatedtxt)
        if accountcreated.is_displayed():
            assert accountcreatedtxt == 'ACCOUNT CREATED!'
        else:
            assert False

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()

    def verifyLoggedinUser(self):
        loggedinuser = self.driver.find_element(By.XPATH, self.btn_loggedinuser_xpath)
        loggedinusertxt = loggedinuser.text
        print(loggedinusertxt)
        if loggedinuser.is_displayed():
            assert loggedinusertxt == f'Logged in as {self.fname}'
        else:
            print("not displayed")


    def clickDeleteAccount(self):
        self.driver.find_element(By.XPATH, self.btn_deleteaccount_xpath).click()

    def verifyAccountDeleted(self):
        deleteaccount = self.driver.find_element(By.XPATH, self.lbl_deleteaccounttxt_xpath)
        deleteaccounttxt = deleteaccount.text
        if deleteaccount.is_displayed():
            assert deleteaccounttxt == 'ACCOUNT DELETED!'
        else:
            assert False

    def verifySignupMsg(self):
        signupmsg = self.driver.find_element(By.XPATH, self.lbl_signupmsg_xpath)
        signupmsgtxt = signupmsg.text
        if signupmsg.is_displayed():
            assert signupmsgtxt == 'Email Address already exist!'
        else:
            assert False