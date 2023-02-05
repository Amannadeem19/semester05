import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

from actionChains import driver

PATH = "E:\semester5\SQE\Selenium\chromedriver.exe"


# opt = webdriver.ChromeOptions()
class LoginTest(unittest.TestCase):
    # def test_loginEmail(self):
    #     print("this is login by email test")
    #     self.assertTrue(True)
    def setUp(self):
        serObj = Service("PATH")
        driver = webdriver.Chrome(service=serObj)
        driver.get("https://facebook.com")

    def test_loginFacebook(self):
        search = driver.find_element("name", "email")
        search.send_keys("amannadeem985@yahoo.com")
        search.send_keys(Keys.RETURN)
        search2 = driver.find_element("name", "pass")
        search2.send_keys("realmadrid2")
        search2.send_keys(Keys.RETURN)
        time.sleep(20)
        driver.quit()
        print("this is login by facebook test")
        self.assertTrue(True)

    def test_loginTwitter(self):
        print("this is login by twitter test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
