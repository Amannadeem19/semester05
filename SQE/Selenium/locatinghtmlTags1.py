import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

PATH = "E:\semester5\SQE\Selenium\chromedriver.exe"
# opt = webdriver.ChromeOptions()

serObj = Service("PATH")

driver = webdriver.Chrome(service=serObj)

driver.get("https://facebook.com")
search = driver.find_element("name", "email")
search.send_keys("amannadeem985@yahoo.com")
search.send_keys(Keys.RETURN)
search2 = driver.find_element("name", "pass")
search2.send_keys("realmadrid2")
search2.send_keys(Keys.RETURN)


time.sleep(20)
driver.quit()



