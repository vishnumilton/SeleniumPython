from PageObjects.ConformPage import ConformPage
from PageObjects.Homepage import Homepage
from PageObjects.PlaceOrder import PlaceOrder
from Utilites.BaseClass import BaseClass
from selenium.webdriver.support.select import Select
from time import sleep


class TestMarkete2e(BaseClass):
    def test_Markete2e(self):
        log = self.getlogger()
        log.info("Market webpage automation is started...")
        homepage = Homepage(self.driver)
        homepage.getSearch().send_keys("ro")
        sleep(2)
        items = homepage.getProduct()
        for i in items:
            name = i.find_element_by_xpath("h4").text
            if name == 'Carrot - 1 Kg':
                log.info(name + "Item has been selected.")
                #assert "pat" in name
                price = i.find_element_by_xpath("p").text
                log.info("Its price is " + price)
                i.find_element_by_css_selector("[type=button]").click()
                log.info("Added to cart !")
        homepage.getCart().click()
        log.info("Went to cart !")
        sleep(2)
        homepage.getPTC().click()
        sleep(2)

        placeorder = PlaceOrder(self.driver)
        placeorder.getPromocode().send_keys("rahulshettyacademy")
        log.info("Applying Coupon...")
        placeorder.getApply().click()
        sleep(8)
        print(self.driver.find_element_by_css_selector(".promoInfo").text)
        log.info("Coupon has been applied successfully !")
        placeorder.getplace().click()
        log.info("Now placing order.")

        conformpage = ConformPage(self.driver)
        country = Select(conformpage.getCountry())
        country.select_by_visible_text("India")
        log.info("Country has been selected !")
        sleep(2)
        conformpage.getagreechkbtn().click()
        log.info("terms and conditions accepted !")
        conformpage.getProceed().click()
        log.info("Hurry ! Your order has been placed successfully.")