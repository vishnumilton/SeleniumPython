from selenium.webdriver.common.by import By


class ConformPage:
    def __init__(self, driver):
        self.driver = driver

    country = (By.XPATH, "//*[@id='root']/div/div/div/div/div/select")
    agreechkbox = (By.CSS_SELECTOR, ".chkAgree")
    proceed = (By.XPATH, "//button[text()='Proceed']")

    def getCountry(self):
        return self.driver.find_element(*ConformPage.country)

    def getagreechkbtn(self):
        return self.driver.find_element(*ConformPage.agreechkbox)

    def getProceed(self):
        return self.driver.find_element(*ConformPage.proceed)