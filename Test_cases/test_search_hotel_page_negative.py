from selenium import webdriver
from PageObjects.login_page_POM import LoginPageActions
from PageObjects.search_hotel_POM import  SearcHotelPageActions
from Test_utilities.customLogger import logGen
from Test_cases import conftest
from time import sleep

class TestSearchHotel:

    def test_search_hotel(self,setup_browser):
        """
        Testcase to input values in the fields provided
        :return:
        """
        self.driver = setup_browser
        logs_obj = logGen.logger()
        loginpage_obj = LoginPageActions(self.driver)
        searchhotel_obj = SearcHotelPageActions(self.driver)

        # Logging into Adactin Hotel Page
        loginpage_obj.login_to_adactin_hotel()
        # self.driver.implicitly_wait()

        searchhotel_obj.click_search()
        sleep(2)

        searchhotel_obj.verifyerrormsg()
        error_text = searchhotel_obj.verifyerrormsg()

        error_msg = 'Please Select a Location'

        if error_text == error_msg:
            logs_obj.info("Test case for Negative Scenario - PASSED")
            print(" Test case for Negative Scenario - PASSED")