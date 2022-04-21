from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("file:///C:/Users/Sunil%20R%20D/Downloads/demo.html")
driver.maximize_window()
sleep(2)
# print(driver.title)
# driver.find_element_by_xpath(r"//a[@class='ico-register']").click()
# driver.find_element_by_css_selector(r"a[class='ico-register']").click()
# res = driver.find_element_by_partial_link_text(r'Reg').text
# print(res)
driver.find_element_by_xpath("//td[text()='Python']/..//input[@type='checkbox']").click()
sleep(2)
# for item in elements:
#     item.click()
#     sleep(2)
# driver.close()
