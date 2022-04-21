from selenium import webdriver
from time import sleep
# from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("./chromedriver")
sleep(2)
driver.get("http://demowebshop.tricentis.com/")


#
# def wait(func):
#     def wrapper(*args,**kwargs):
#         locator = args[0]
#         wait_ = WebDriverWait(driver,20)
#         return func(*args,**kwargs)
#     return wrapper
#
#
#
# @wait

def test_register():

    def click_element(locator):
        driver.find_element(*locator).click()
        sleep(2)
    #
    # @wait

    def enter_text(locator, value):
        driver.find_element(*locator).clear()
        driver.find_element(*locator).send_keys(value)
        sleep(2)

    click_element(("link text", "Register"))
    click_element(("id", 'gender-male'))
    enter_text(("id", "FirstName"), value="hello")

    driver.quit()
