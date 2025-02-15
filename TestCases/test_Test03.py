from Utilities.readproperties import readConfig
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from Utilities import ExcelLoginUtils


class Test03_LoginDDT:

    baseURL = readConfig.getApplicationURL()
    file_path = "C:\\Users\\Bhavesh\\PycharmProjects\\AutoExceriseApp\\TestData\\LoginData.xlsx"



    def test_LoginDDT(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.verifyTitle()
        self.hp.clickSignupLogin()
        self.lp = LoginPage(self.driver)
        self.lp.verifyLogintxtdisplayed()
        self.rows = ExcelLoginUtils.getRowCount(self.file_path,"Sheet1")
        for r in range(2,self.rows+1):
            self.username = ExcelLoginUtils.readData(self.file_path,"Sheet1",r,1)
            self.password = ExcelLoginUtils.readData(self.file_path,"Sheet1",r,2)
            self.exp = ExcelLoginUtils.readData(self.file_path,'Sheet1',r,3)
            self.lp.setEmail(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

