from selenium import webdriver
# from selenium_wrapper import Selenium_Wrapper
from time import sleep

driver = webdriver.Chrome("./chromedriver")
driver.get("http://demowebshop.tricentis.com/")

def test_log_in():

    def click_element(locator):
        driver.find_element(*locator).click()
        sleep(2)

    def enter_text(locator,value):
        driver.find_element(*locator).clear()
        driver.find_element(*locator).send_keys(value)
        sleep(2)

    click_element(("xpath","//a[text()='Log in']"))
    enter_text(("id", "Email"), value="hello@glkk.com")
    enter_text(("id", "Password"), value="hvjkjgkdbbd")

    driver.quit()