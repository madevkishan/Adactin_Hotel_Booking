from selenium import webdriver
from PageObjects.login_page_POM import LoginPageActions
from PageObjects.search_hotel_POM import SearcHotelPageActions
from PageObjects.select_hotel_POM import SelectHotelPageActions
from PageObjects.book_hotel_POM import BookHotelPageActions
from Test_utilities.customLogger import logGen
from Test_cases import conftest
from time import sleep

class TestBookHotel:

    def test_book_hotel(self,setup_browser):
        """
        Testcase to Book Hotel
        :return:
        """
        self.driver = setup_browser
        logs_obj = logGen.logger()
        loginpage_obj = LoginPageActions(self.driver)
        searchhotel_obj = SearcHotelPageActions(self.driver)
        selecthotel_obj = SelectHotelPageActions(self.driver)
        bookhotel_obj = BookHotelPageActions(self.driver)
        # Logging into Adactin Hotel Page
        loginpage_obj.login_to_adactin_hotel()
        # self.driver.implicitly_wait()

        searchhotel_obj.enter_location()
        # sleep(1)

        searchhotel_obj.enter_hotels()
        # sleep(1)

        searchhotel_obj.enter_roomtype()
        # sleep(1)

        searchhotel_obj.enter_numofrooms()
        # sleep(1)

        searchhotel_obj.enter_checkindate()
        # sleep(1)

        searchhotel_obj.enter_checkoutdate()
        # sleep(1)

        searchhotel_obj.enter_adult()
        # sleep(1)

        searchhotel_obj.enter_children()
        # sleep(1)

        searchhotel_obj.click_search()
        # sleep(1)

        selecthotel_obj.click_select()
        # sleep(1)

        selecthotel_obj.click_continue()
        # sleep(3)

        bookhotel_obj.enter_firstname()
        # sleep(2)

        bookhotel_obj.enter_lastname()
        # sleep(1)

        bookhotel_obj.enter_billingaddress()
        sleep(1)

        bookhotel_obj.enter_creditcard_num()
        sleep(1)

        bookhotel_obj.enter_creditcard_type()
        sleep(1)

        bookhotel_obj.enter_expmonth()
        sleep(1)

        bookhotel_obj.enter_expyear()
        sleep(2)

        bookhotel_obj.enter_cvv_num()
        sleep(1)

        bookhotel_obj.click_booknow()
        sleep(1)

