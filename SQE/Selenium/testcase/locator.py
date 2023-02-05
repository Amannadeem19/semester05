# all the css selector, tags are located in a centralized location

from selenium.webdriver.common.by import By


class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit")


class SearchResultsPageLocators(object):
    pass
