from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def wait_web(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    def wait_presence(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )

