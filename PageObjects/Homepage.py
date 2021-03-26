from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    search = (By.CLASS_NAME, "search-keyword")
    product = (By.XPATH, "//div[@class='products']/div")
    cart = (By.XPATH, "//*[@id='root']/div/header/div/div[3]/a[4]/img")
    proceedToCheck = (By.CSS_SELECTOR, "button[type='button']")

    def getSearch(self):
        return self.driver.find_element(*Homepage.search)

    def getProduct(self):
        return self.driver.find_elements(*Homepage.product)

    def getCart(self):
        return self.driver.find_element(*Homepage.cart)

    def getPTC(self):
        return self.driver.find_element(*Homepage.proceedToCheck)
