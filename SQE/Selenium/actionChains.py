from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "E:\semester5\SQE\Selenium\chromedriver.exe"

SerObj = Service(PATH)

driver = webdriver.Chrome(service=SerObj)
driver.get("http://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = cookie_count.text
    print(count)
    
    
 

            