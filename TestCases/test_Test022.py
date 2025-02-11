from Utilities.readproperties import readConfig
from pageObjects.HomePage import HomePage


class Test022_AddCartFromRecommendation:
    baseURL = readConfig.getApplicationURL()

    def test_addCartFromRecommendation(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.hp = HomePage(self.driver)
        self.hp.scrollDowntoFooter()
        self.hp.addRecommendProductToCart()