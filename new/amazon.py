from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)
driver.find_element_by_id("searchDropdownBox").click()
sleep(2)
driver.find_element_by_xpath("//option[text()='Electronics']").click()
sleep(2)
driver.find_element_by_xpath("//input[@value='Go']").click()
sleep(2)
driver.find_element_by_xpath("//span[@class='a-truncate-cut']").click()
sleep(1)
# driver.find_element_by_xpath("//input[@id='add-to-cart-button']").click()
# sleep(1)
# driver.find_element_by_xpath("//input[@class='a-button-input']").click()
# sleep(1)