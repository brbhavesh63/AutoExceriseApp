from Utilities.readproperties import readConfig
from pageObjects.HomePage import HomePage
from pageObjects.ProductDetailPage import ProductDetailPage
from pageObjects.ProductPage import ProductPage


class Test021_AddReview:

    baseURL = readConfig.getApplicationURL()
    reviewname = readConfig.getReviewerName()
    reviewemail = readConfig.getReviewerEmail()
    reviewdesc = readConfig.getReviewerDesc()

    def test_AddReview(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.clickProducts()
        self.hp.scrolltoProduct()
        self.pp = ProductPage(self.driver)
        self.pp.clickFirstProducts()
        self.hp.scrollDowntoFooter()
        self.pd = ProductDetailPage(self.driver)
        self.pd.sendReview(self.reviewname,self.reviewemail,self.reviewdesc)
        self.pd.verifySuccessReview()
