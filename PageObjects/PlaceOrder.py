from selenium.webdriver.common.by import By


class PlaceOrder:
    def __init__(self, driver):
        self.driver = driver

    promocode = (By.CLASS_NAME, "promoCode")
    apply = (By.CSS_SELECTOR, ".promoBtn")
    place = (By.XPATH, "//*[@id='root']/div/div/div/div/button")

    def getPromocode(self):
        return self.driver.find_element(*PlaceOrder.promocode)

    def getApply(self):
        return self.driver.find_element(*PlaceOrder.apply)

    def getplace(self):
        return self.driver.find_element(*PlaceOrder.place)