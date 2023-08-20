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

        searchhotel_obj.enter_location()
        sleep(1)

        searchhotel_obj.enter_hotels()
        sleep(1)

        searchhotel_obj.enter_roomtype()
        sleep(1)

        searchhotel_obj.enter_numofrooms()
        sleep(1)

        searchhotel_obj.enter_checkindate()
        sleep(1)

        searchhotel_obj.enter_checkoutdate()
        sleep(1)

        searchhotel_obj.enter_adult()
        sleep(1)

        searchhotel_obj.enter_children()
        sleep(1)

        searchhotel_obj.click_search()
        sleep(1)