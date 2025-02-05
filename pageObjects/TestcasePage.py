from selenium import webdriver

class TestCasePage:

    def __init__(self,driver):
        self.driver = driver

    def verifyTitle(self):
        act_title = self.driver.title
        print(act_title)
        if act_title == 'Automation Practice Website for UI Testing - Test Cases':
            assert True
        else:
            assert False