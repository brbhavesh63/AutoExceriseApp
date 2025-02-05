from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture()

def setup():
    # if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_extension("C:\\Users\\Bhavesh\\PycharmProjects\\AutoExceriseApp\\TestData\\ubloackcrx.crx")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-save-password-bubble")
        # Disable popups (e.g., "Save Password" notifications)
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        print("Launching Chrome Browser")
        driver.maximize_window()
    #
    # elif browser == 'firefox':
    #     options = webdriver.FirefoxOptions()
    #     options.add_argument("--detach")  # Note: Detach is not natively supported by Firefox; this may need other handling
    #     driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
    #     print("Launching Firefox Browser")
    #
    # else:
    #     options = webdriver.EdgeOptions()
    #     options.add_argument("--detach")  # Note: Detach is not natively supported by Edge; this may need other handling
    #     driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
    #     print("Launching Edge Browser")

        return driver