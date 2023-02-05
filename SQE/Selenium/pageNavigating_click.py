from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "E:\semester5\SQE\Selenium\chromedriver.exe"
serobj = Service(PATH)
driver = webdriver.Chrome(service=serobj)

driver.get("https://techwithtim.net")

link = driver.find_element(By.LINK_TEXT, 'Python Programming')
link.click()

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Beginner Python Tutorials'))
    )
    element.click()

    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'sow-button-19310003'))
    )
    element.click()

    driver.back()
    driver.back()
    driver.forward()

except:
    driver.quit()

time.sleep(20)
