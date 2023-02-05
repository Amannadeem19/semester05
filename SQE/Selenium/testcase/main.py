import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import page


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        print("setup called")
        self.PATH = "E:\semester5\SQE\Selenium\chromedriver.exe"
        self.service = Service(self.PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://www.python.org/")

    # this function is called when the unit test is started it dont need to separately called, as it starts from test

    # def test_example(self):
    #     print("test1")
    #     assert False

    # def test_example2(self):
    #     print("test2")
    #     assert False
# Gui testing
    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "Pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found()

        # runs after the test case is finished  

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
