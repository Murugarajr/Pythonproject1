"""First Selenium file- 02/12/2019
Test program for chrome configuration"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\Admin\\PycharmProjects\\Seleniumtest\\Driver\\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("http://google.co.in")
driver.find_element_by_name("q").send_keys("nishaptham")
# driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

time.sleep(4)
driver.maximize_window()
print("Tested sucessfully!")
driver.quit()
