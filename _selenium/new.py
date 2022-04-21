from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
""" 1) """
#lanches a new chrome browser
driver = webdriver.Chrome("./chromedriver")
# driver.get("https://www.google.co.in/")
sleep(2)
#navigate to google

# ##########   By using xpath

# driver.get("")
#
# driver.find_element_by_xpath("//a[@class='ico-register']").click()
# sleep(2)
#
# driver.find_element_by_xpath("//input[@id='gender-male']").click()
# sleep(2)
#
# driver.find_element_by_xpath("//input[@id='FirstName']").send_keys("sunil")
# sleep(2)
#
# driver.find_element_by_xpath("//input[@id='LastName']").send_keys("kumar")
# sleep(2)
#
# driver.find_element_by_xpath("//input[@id='Email']").send_keys("sunil@gmail.com")
# sleep(2)
#
# driver.find_element_by_xpath("//input[@id='Password']").send_keys("1234567890")
# sleep(2)
#
# driver.find_element_by_xpath("//input[@id='ConfirmPassword']").send_keys("1234567890")
# sleep(2)
#
# driver.find_element_by_xpath("//input[@id='register-button']").click()
# sleep(2)

#####################################

# driver.find_element_by_link_text("Register").click()
# sleep(2)
#
# driver.find_element_by_id("gender-male").click()
# sleep(2)
#
# driver.find_element_by_name("FirstName").send_keys("hello")
# sleep(2)
#
# driver.find_element_by_name("LastName").send_keys("world")
# sleep(2)
#
# driver.find_element_by_id("Email").send_keys("helloworld@gmail.com")
# sleep(2)
#
# driver.find_element_by_name("Password").send_keys("password123")
# sleep(2)
#
# driver.find_element_by_name("ConfirmPassword").send_keys("password123")
# sleep(2)
#
# driver.find_element_by_id("register-button").click()
# sleep(2)
# driver.close()

###########   css_selector

# driver.get("file:///C:/Users/Sunil%20R%20D/Downloads/css_selector.html")
# sleep(2)
#
# driver.find_element_by_css_selector("input[type='text']").send_keys("hello")
# sleep(2)
#
# driver.find_element_by_css_selector("input[type='password']").send_keys("word")
# sleep(2)


""" 2) to click the required radio button"""

# driver.get("file:///C:/Users/Sunil%20R%20D/Downloads/demo.html")
# sleep(2)
# links = driver.find_elements_by_xpath("//a")
# for item in links:
#     print(item.text)
#     sleep(2)
#
######################
# click on particular sub string

# driver.get("https://www.python.org/")
# links = driver.find_elements_by_xpath("//a")
# for item in links:
#     link_text = item.text.strip()
#     if "python" in link_text:
#         print(link_text)
#         sleep(2)

# to get attribute value (href)
# for item in links:
#     link_text = item.text.strip()
#     url = item.get_attribute("href")
#     if "python" in link_text:
#         print(f"{link_text}:{url}")

##########################
# to click particular link

# driver.get("https://www.python.org/downloads/")
# sleep(2)
#
# driver.find_element_by_xpath("//a[text()='Python 3.9.9']/../..//a[text()='Release Notes']").click()
# sleep(2)


##############################
# to click on the checkbox

# driver.get("file:///C:/Users/Sunil%20R%20D/Downloads/demo.html")
# sleep(2)
# elements = driver.find_elements_by_xpath("//input[@name='download']")
# for element in elements[::2]:
#     element.click()
#     sleep(.2)
# print(len(elements))


# cars = driver.find_element_by_id("standard_cars")
# s = Select(cars)
# all_options = s.options
#
# text_options = [item.text for item in all_options]
#
# for item in text_options:
#     s.select_by_visible_text(item)
#     sleep(.2)
# print(text_options)
# url = driver.current_url
# print(f"current working url is {url}")
# driver.close()



# companies = ['MGFT','FB','AA','AAPL']
# for company in companies:
#     _xpath = f"//td[text()='{company}']/.. //td[@class='price']"
#     share_price = float(driver.find_element_by_xpath(_xpath).text)
#     print(f'{company} : {share_price}')

################
# driver.get("https://testproject.io/?utm_source=google-ads&utm_campaign=testproject_june&utm_agid=102398253963&utm_term=web%20application%20test&creative=472543965813&device=c&placement&gclid=CjwKCAiAjoeRBhAJEiwAYY3nDMT_WqiV4aXxG2NFqsXNgTk23y2N0yk-o5zVk5RLuxl_sAwKNqGbSRoChh4QAvD_BwE")
# sleep(2)
# driver.find_element_by_link_text('Login').click()




####################

# driver.find_element_by_xpath("//label[text()='Good']/..//input[@type='radio']").click()
# driver.find_element_by_id("vote-poll-1").click()
# """ 3) """
#
##########################

# Date picker popup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("./chromedriver.exe")


from selenium.common.exceptions import NoSuchElementException

# driver.get("https://www.goibibo.com/")
# driver.maximize_window()
# sleep(5)
#
# driver.find_element_by_xpath("//span[text()='Departure']").click()
# sleep(2)

# driver.find_element_by_xpath("//span[text()='Departure']").click()
# sleep(2)
#
# # _month_year = "July 2022"
# # _day = "5"
# def select_date(_month_year,_day):
#     for _ in range(12):
#         try:
#             driver.find_element_by_xpath(f"//div[text()='{_month_year}']/../..//p[text()='{_day}']").click()
#             sleep(2)
#             break
#         except NoSuchElementException:
#             driver.find_element_by_xpath("//span[@aria-label='Next Month']").click()
#             sleep(1)
#             continue
#
# print(select_date("July 2022", "5"))
#
# driver.close()



############    SYNCHRONIZATION    ################

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

# driver.get("file:///C:/Users/Sunil%20R%20D/Downloads/demo.html")
# #to create an object instance
# wait = WebDriverWait(driver, timeout=10)
# #wait until the textbox is visible
# wait.until(expected_conditions.visibility_of_element_located(("name", "fname")))
# driver.find_element_by_name("fname").send_keys("hello")

##################

## wait for progress bar to complete 100% in demo html page

# driver.get(" progressbar")
# sleep(2)
#
# # click on Click Me button on the demo-webpage
# driver.find_element_by_xpath("//button[text()='Click Me']").click()
# wait = WebDriverWait(driver, timeout=10)
# #wait until the progress bar is loaded completely(100%) and visible on the webpage
#
# wait.until(expected_conditions.visibility_of_element_located(("xpath", "//div[text()="100%"")))
# print("Done")

##################

## create a function to perform a action like click, enter text

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located
# from selenium.webdriver.common.by import By
#
#
# driver.get("http://demowebshop.tricentis.com/")
# sleep(2)
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __call__(self, driver):
#         result = super().__call__(driver)
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         else:
#             return False
# def wait(func):
#     def wrapper(*args,**kwargs):
#         locator = args[0]
#         wait_ = WebDriverWait(driver, 20)
#         v = _visibility_of_element_located(locator)
#         wait_.until(v)
#         return func(*args,**kwargs)
#     return wrapper
#
#
# @wait
# def click_element(locator):
#     driver.find_element(*locator).click()
#
# @wait
# def enter_text(locator, value):
#     driver.find_element(*locator).click()
#     driver.find_element(*locator).send_keys(value)
#
#
# click_element(("link text", "Register"))
# enter_text((By.ID, "FirstName"), value="hello")

#







# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import visibility_of_element_located, alert_is_present
# from selenium.webdriver.remote.webelement import WebElement
# from config import Config
#
# # Launches a new chrome browser
# driver = webdriver.Chrome("./chromedriver")
# sleep(2)
# driver.maximize_window()
# driver.get(Config.URL)
# sleep(3)
#
# class _visibility_of_element_located(visibility_of_element_located):
#     def __call__(self, driver):
#         result = super().__call__(driver)
#         if isinstance(result, WebElement):
#             return result.is_enabled()
#         else:
#             return False
#
# def wait(func):
#     def wrapper(*args, **kwargs):       # args = (self, ("link text", "Register"))
#         # args = (("name", "FirstName"), ) kwargs = {value="hello"}
#         instance = args[0]
#         locator = args[1]
#         wait_ = WebDriverWait(instance.driver, Config.MAX_TIMEOUT)
#         v = _visibility_of_element_located(locator)
#         wait_.until(v)
#         # click_element(("link text", "Register"))
#         # enter_text(("name", "fname"), value="hello")
#         return func(*args, **kwargs)        # actual generic func gets executed
#     return wrapper
#
# class Selenium_Wrapper:
#     def __init__(self, driver):
#         self.driver = driver
#
#     @wait
#     def click_element(self, locator):
#         """
#         Clicks on the element
#         useage: click_element("id", "register")
#         """
#         self.driver.find_element(*locator).click()       # find_element("link text", "register")
#
#     @wait
#     def enter_text(self, locator, *, value):
#         """enters something inside the text box"""
#         self.driver.find_element(*locator).clear()
#         self.driver.find_element(*locator).send_keys(value)
#
#     @wait
#     def select_item(self, locator, *, item):
#         """Selects some item from the listbox"""
#         element = self.driver.find_element(*locator)
#         s = Select(element)
#         if isinstance(item, str):
#             s.select_by_visible_text(item)
#         elif isinstance(item, int):
#             s.select_by_index(item)
#         else:
#             raise TypeError
#
# s = Selenium_Wrapper(driver)        # passing the driver instance that is created in 15th line
#
# s.click_element((By.LINK_TEXT, "Register"))
# s.click_element((By.ID, "gender-male"))
# s.enter_text((By.NAME, "FirstName"), value="hello")
# s.enter_text((By.NAME, "LastName"), value="world")
# s.enter_text((By.ID, "Email"), value="hello.world@company.com")
# s.enter_text((By.ID, "Password"), value="Password123")
# s.enter_text((By.ID, "ConfirmPassword"), value="Password123")
# s.click_element((By.ID, "register-button"))
# driver.close()

# driver = webdriver.Chrome("./chromedriver")
# driver.get("http://demowebshop.tricentis.com/")
# sleep(2)

##############################
#validate the price of all the gatgets against the expected price

# driver.get("http://demowebshop.tricentis.com/")
# sleep(2)
#####
# dictionary with Gadget name and its actual_price price
# for all names
# elements_ = driver.find_elements_by_xpath("//h2[@class='product-title']")
# names_ = [item.text for item in elements_]
# # for all price
# elements_ = driver.find_elements_by_xpath("//div[@class='prices']")
# price_ = [item.text for item in elements_]
#
# dict_ = {a: b for a, b in zip(names_,price_)}
# print(dict_)  ## {'$25 Virtual Gift Card': '25.00', '14.1-inch Laptop': '1590.00', 'Build your own cheap computer': '800.00', 'Build your own computer': '1200.00', 'Build your own expensive computer': '1800.00', 'Simple Computer': '800.00'}
#####

# expected_price = {"$25 Virtual Gift Card": 25.00,
#                   "14.1-inch Laptop": 1590.00,
#                   "Build your own cheap computer": 800.00,
#                   "Build your own computer": 1200.00,
#                   "Build your own expensive computer": 1800.00,
#                   "Simple Computer": 800.00}
#
# # Iterate through the dictionary, get the gadget name and its corresponding expected price.
# for gadget,price in expected_price.items():
#     xpath = f"//a[text()='{gadget}']/../..//span[@class='price actual-price']"
#     actual_price = driver.find_element_by_xpath(xpath).text
#     # compare actual and expected price
#     if float(actual_price) == price:
#         print("PASS")
#     else:
#         print("FAIL")
#########################################
import re
# driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/sunglasses")
# sleep(2)
# names = driver.find_elements_by_xpath("//h3[@class='art-name']")
# res1 = [item.text for item in names]
# price = driver.find_elements_by_xpath("//div[@class='art-price-block']")
# res2 = [item.text for item in price]
#
# dict_ = {a: b for a, b in zip(res1, res2)}
# print(dict_)
#Dictionary with sun_glass name and its expected prices
# sun_glasses = {'Sunglasses Aero': 139.00, 'ORIGINAL COLLECTION': 149.00, 'Custom Sunglasses': 179.00}

# for glass, expected_price in sun_glasses.items():
#     _xpath = f"//span[text()='{glass}']/../../..//span[@class='art-price']"
#     price_tag = driver.find_element_by_xpath(_xpath).text
#     price = re.findall(r'\d+.\d+',price_tag)
#
#     print(price)  # ['139.00']
    # if float(price[0]) == expected_price:
    #     print("PASS")
    # else:
    #     print("FAIl")

#########################################
# Get the price tag of all the new products in smart bear webpage

# driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/newproducts")
# sleep(2)
# prices = driver.find_elements_by_xpath("//div[@class='art-price-block']")
# for item in prices:
#     price = item.text
#     _price = re.findall(r'\d+,?\d*\.\d+',price)[0]
#     print(_price)
#     sleep(2)

######################################
# Get the share price Dynamically

# driver.get("https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market")
# sleep(5)
#
# companies = ["TCS", "WIPRO", "MARUTI"]
#
# # Print the headers(company names)
# for company in companies:
#     print(f"{company:>15}",end='')
# #print an empty line after headers
# print()
# print('-'*55)
#
# #while loop to monitot the share price every 5 seconds
# while True:
#     for company in companies:
#         share_price = driver.find_element("xpath",f"//a[text()='{company}']/../..//td[7]").text
#         print(f"{share_price}",end='  ')
#     print()
#     sleep(2)
#############################################

#GET THE LINK TEXT OF ALL LINKS PRESENT IN LEFT NAVIGATION BAR
#IN DEMOWEBSHOP WEBPAGE

# driver.get("http://demowebshop.tricentis.com/")
# sleep(2)
# elements = driver.find_elements_by_xpath("//div[@class='block block-category-navigation']//a")
# for element in elements:
#     print(element.text)
#     sleep(1)
##################################################

# GET LINK TEXT OF ALL THE JOB TITLES IN SEARCH RESULTS OF
# MONSTER.COM

# driver.get("https://www.monsterindia.com/")
# driver.maximize_window()
# sleep(2)
#
# driver.find_element_by_xpath("//input[@id='SE_home_autocomplete']").send_keys("python")
# sleep(2)
# driver.find_element_by_xpath("//strong[text()='Python']").click()
# sleep(2)
# driver.find_element_by_xpath("//input[@value='Search']").click()
# sleep(2)
#
# # job titles
# job_titles = driver.find_elements_by_xpath("//div[@class='job-tittle']/h3/a")
# for jobs in job_titles:
#     print(jobs.text)
#     sleep(0.5)

###########################################
# EXTRACTING TSHIRT NAME AND DISCOUNT OF ALL DISCOUNTED
# TSHIRTS IN MYNTRA.COM

# driver.get("https://www.myntra.com/boys-tshirts")
# driver.maximize_window()
# sleep(3)
# ts_names = driver.find_elements_by_xpath("//h3[@class='product-brand']")
# ts_discount = driver.find_elements_by_xpath("//span[@class='product-discountPercentage']/../..//h4[@class='product-product']")
# # get discounts
# discount = [item.text for item in ts_discount]
# # get names
# names = [item.text for item in ts_names]
#
# actual_discount = []
# # building a list of tuples with names and discount pair
#
# for name,item in zip(names,discount):
#     actual_discount.append((name,item))
#
# print(actual_discount)
############################################

#FILTERING ONLY “PEPE JEANS” T-SHIRTS (VALIDATE FILTER FUNCTIONALITY)

# driver.get("https://www.myntra.com/boys-tshirts")
# sleep(2)
#
# driver.find_element_by_xpath("//label[@class='vertical-filters-label common-customCheckbox'][1]").click()
# sleep(2)

#################################
#
# driver.get("http://demowebshop.tricentis.com/")
# sleep(2)
#
# driver.find_element_by_xpath("//a[text()='Twitter']").click()
# sleep(2)
#
# handles = driver.window_handles
#
# driver.switch_to.window(handles[1])
# sleep(5)
#
# driver.switch_to.window(handles[0])
# sleep(2)



###############################





















##

# d = {"a": "hello", "b": 100, "c":10.1, "d": "world"}
# res = {}
# for item,value in d.items():
#     if isinstance(value,str):
#         res[item] = value[::-1]
#     else:
#         res[item] = value
# print(res)