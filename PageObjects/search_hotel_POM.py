from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Test_utilities.customLogger import logGen
from Test_data import credentials
from Test_locators.test_locators import LoginPageLocators,SearchHotelLocators

class SearcHotelPageActions:
    def __init__(self,driver):
        # self.login_loc_obj = LoginPageLocators()
        self.search_loc_obj = SearchHotelLocators()
        self.logs_obj = logGen.logger()
        self.driver = driver
        self.driver.get(credentials.url)
        self.driver.maximize_window()
        # self.driver.implicitly_wait(10)

    def enter_location(self):
        """
        find the webelement for Location dropdown and select is using an index,value,...

        :return:
        """
        location_we = self.driver.find_element(By.XPATH, self.search_loc_obj.location_loc_dd_xpath)
        select_var = Select(location_we)
        select_var.select_by_value('Sydney')
        self.logs_obj.info("Sydney selected")

    def enter_hotels(self):
        """
        find the webelement for Hotels dropdown and select is using an index,value,...

        :return:
        """
        hotels_we = self.driver.find_element(By.XPATH, self.search_loc_obj.hotels_loc_dd_xpath)
        select_var = Select(hotels_we)
        select_var.select_by_value('Hotel Creek')
        self.logs_obj.info("Hotel Creek selected")

    def enter_roomtype(self):
        """
        find the webelement for 'RoomType' dropdown and select is using an index,value,...

        :return:
        """
        roomtype_we = self.driver.find_element(By.XPATH, self.search_loc_obj.roomtype_loc_dd_xpath)
        select_var = Select(roomtype_we)
        select_var.select_by_value('Standard')
        self.logs_obj.info("Standard selected")

    def enter_numofrooms(self):
        """
        find the webelement for 'Number of Rooms' dropdown and select is using an index,value,...

        :return:
        """
        numofrooms_we = self.driver.find_element(By.XPATH, self.search_loc_obj.numofrooms_loc_dd_xpath)
        select_var = Select(numofrooms_we)
        select_var.select_by_value('2')
        self.logs_obj.info("Two rooms selected")

    def enter_checkindate(self):
        """
        find the webelement for check-in date

        :return:
        """
        checkindate_we = self.driver.find_element(By.XPATH, self.search_loc_obj.checkin_loc_txt_xpath)
        checkindate_we.clear()
        # checkindate_we.send_keys("20/08/2023")
        checkindate_we.send_keys("13/07/2023") # uncomment this for negative testcase
        self.logs_obj.info("Check In dates Entered")

    def enter_checkoutdate(self):
        """
        find the webelement for check-in date

        :return:
        """
        checkoutdate_we = self.driver.find_element(By.XPATH, self.search_loc_obj.checkout_loc_txt_xpath)
        checkoutdate_we.clear()
        # checkoutdate_we.send_keys("22/08/2023")
        checkoutdate_we.send_keys("17/07/2023") # uncomment this for negative testcase
        self.logs_obj.info("Check out dates Entered")


    def enter_adult(self):
        """
        find the webelement for 'Number of Adults' from the dropdown and select is using an index,value,...

        :return:
        """
        adult_we = self.driver.find_element(By.XPATH, self.search_loc_obj.adult_loc_dd_xpath)
        select_var = Select(adult_we)
        select_var.select_by_value('3')
        self.logs_obj.info("3 Adult selected")

    def enter_children(self):
        """
        find the webelement for 'Number of Adults' from the dropdown and select is using an index,value,...

        :return:
        """
        children_we = self.driver.find_element(By.XPATH, self.search_loc_obj.children_loc_dd_xpath)
        select_var = Select(children_we)
        select_var.select_by_value('4')
        self.logs_obj.info("4 children selected")

    def click_search(self):
        """
        find the webelement for SEARCH Button

        :return:
        """
        search_we = self.driver.find_element(By.XPATH, self.search_loc_obj.search_loc_btn_xpath)
        search_we.click()
        self.logs_obj.info("Search button clicked")

    def verifyerrormsg(self):
        """
        Verifying for Error Message
        :return:
        """

        verify_we = self.driver.find_element(By.XPATH,self.search_loc_obj.errrormsg_loc_xpath)
        verify_txt = verify_we.text
        return verify_txt