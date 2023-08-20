from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Test_utilities.customLogger import logGen
from Test_data import credentials
from Test_locators.test_locators import LoginPageLocators,SearchHotelLocators,SelectHotelLocators

class SelectHotelPageActions:
    def __init__(self,driver):
        self.select_loc_obj = SelectHotelLocators()
        self.logs_obj = logGen.logger()
        self.driver = driver
        self.driver.get(credentials.url)
        self.driver.maximize_window()

    def click_select(self):
        """
        Click on the option...
       :return:
        """
        clickselect_we = self.driver.find_element(By.XPATH, self.select_loc_obj.selecthotel_loc_radio_xpath)
        clickselect_we.click()
        self.logs_obj.info("Option selected")

    def click_continue(self):
        """
        Click on the continue button...
       :return:
        """
        clickcontinue_we = self.driver.find_element(By.XPATH, self.select_loc_obj.continue_loc_btn_xpath)
        clickcontinue_we.click()
        self.logs_obj.info("Continue Button selected")

    def verifyerrormsg(self):
        """
        Verifying for Error Message
        :return:
        """

        verify_we = self.driver.find_element(By.XPATH, self.select_loc_obj.errormsg_select_loc_xpath)
        verify_txt = verify_we.text
        return verify_txt