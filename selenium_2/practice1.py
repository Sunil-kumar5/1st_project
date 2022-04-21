from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
driver.maximize_window()
driver.minimize_window()
current_title = driver.title
print(current_title)
url = driver.current_url
print(url)
sleep(5)

driver.refresh()
# driver.quit()
# driver.close()
