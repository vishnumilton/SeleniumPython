from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome("c:\webdriver\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_class_name("search-keyword").send_keys("ro")
sleep(2)
items = driver.find_elements_by_xpath("//div[@class='products']/div")
for i in items:
    name = i.find_element_by_xpath("h4").text
    if name == 'Carrot - 1 Kg':
        print(name)
        print(i.find_element_by_xpath("p").text)
        i.find_element_by_css_selector("[type=button]").click()
driver.find_element_by_xpath("//*[@id='root']/div/header/div/div[3]/a[4]/img").click()
sleep(2)
driver.find_element_by_css_selector("button[type='button']").click()
sleep(2)
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
sleep(8)
print(driver.find_element_by_css_selector(".promoInfo").text)
driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/button").click()
country = Select(driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/select"))
country.select_by_visible_text("India")
sleep(2)
driver.find_element_by_css_selector(".chkAgree").click()
driver.find_element_by_xpath("//button[text()='Proceed']").click()