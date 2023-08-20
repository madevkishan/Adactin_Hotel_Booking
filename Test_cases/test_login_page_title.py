from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.login_page_POM import LoginPageActions
from Test_data import credentials
from Test_locators.test_locators import LoginPageLocators

class TestLoginTitle:

    def test_login_page_title(self,setup_browser):
        """
        Testcase to test the title of our webpage
        :return:
        """
        self.driver = setup_browser
        login_obj = LoginPageActions(driver=setup_browser)
        login_obj.login_to_adactin_hotel()

        # title_of_page() == expected_title

# TestLoginTitle().test_login_page_title()

