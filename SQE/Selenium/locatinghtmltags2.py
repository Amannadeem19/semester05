from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "E:\semester5\SQE\Selenium\chromedriver.exe"
# opt = webdriver.ChromeOptions()

serObj = Service("PATH")

driver = webdriver.Chrome(service=serObj)

driver.get("https://techwithtim.net")
search = driver.find_element("name", "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements(By.TAG_NAME, "article")
    for value in articles:
        header = value.find_element(By.CLASS_NAME, "entry-summary")
        print(header.text)

finally:
    driver.quit()
