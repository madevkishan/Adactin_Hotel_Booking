from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Test_utilities.customLogger import logGen
# from  selenium.webdriver.
from Test_data import credentials
from Test_locators.test_locators import LoginPageLocators,SearchHotelLocators,BookHotelLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookHotelPageActions:
    def __init__(self,driver):
        # self.login_loc_obj = LoginPageLocators()
        self.search_loc_obj = SearchHotelLocators()
        self.book_loc_obj = BookHotelLocators()
        self.logs_obj = logGen.logger()
        self.driver = driver
        self.driver.get(credentials.url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,10)

    def enter_firstname(self):
        """
        Enter Firstname Textbox
        :return:
        """
        firstname_we = self.driver.find_element(By.NAME, self.book_loc_obj.firstname_loc_txt_name)
        firstname_we.clear()
        firstname_we.send_keys("Madhuuuuuuu")


    def enter_lastname(self):
        """
        Enter lastname Textbox
        :return:
        """
        lastname_we = self.driver.find_element(By.NAME, self.book_loc_obj.lastname_loc_txt_name)
        lastname_we.clear()
        lastname_we.send_keys("PPPPPPP")

    def enter_billingaddress(self):
        """
        Enter BillingAddress Textbox
        :return:
        """
        billingaddr_we = self.driver.find_element(By.NAME, self.book_loc_obj.addr_loc_txt_name)
        billingaddr_we.clear()
        billingaddr_we.send_keys("ABC  EFG  BJFYU bjhi")

    def enter_creditcard_num(self):
        """
        Enter Creditcard Number Textbox
        :return:
        """
        creditcardnum_we = self.driver.find_element(By.NAME, self.book_loc_obj.ccnum_loc_txt_name)
        creditcardnum_we.clear()
        creditcardnum_we.send_keys("5365776656625")

    def enter_creditcard_type(self):
        """
        Select Creditcard Type from the dropdown
        :return:
        """
        creditcardtype_we = self.driver.find_element(By.XPATH, self.book_loc_obj.cctype_loc_dd_xpath)
        cctype_var = Select(creditcardtype_we)
        cctype_var.select_by_value('MAST')
        self.logs_obj.info("Mastercard selected")

    def enter_expmonth(self):
        """
        Select Expiry Month from the dropdown
        :return:
        """
        expmonth_we = self.driver.find_element(By.XPATH, self.book_loc_obj.expmonth_loc_dd_xpath)
        expmonth_var = Select(expmonth_we)
        expmonth_var.select_by_value('2')
        self.logs_obj.info("February Month selected")

    def enter_expyear(self):
        """
        Select Expiry Year from the dropdown
        :return:
        """
        expyear_we = self.driver.find_element(By.XPATH, self.book_loc_obj.expyear_loc_dd_xpath)
        expyear_we = Select(expyear_we)
        expyear_we.select_by_value('2024')
        self.logs_obj.info("2024 Year selected")

    def enter_cvv_num(self):
        """
        Enter CVV Number Textbox
        :return:
        """
        cvvnum_we = self.wait.until(EC.element_to_be_clickable((By.ID, self.book_loc_obj.cvv_loc_txt_id)))
        # cvvnum_we.clear()
        cvvnum_we.send_keys("5555")
        self.logs_obj.info("CVV number entered")

    def click_booknow(self):
        """
        Click on BOOKNOW button
        :return:
        """
        booknow_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.book_loc_obj.booknow_loc_btn_xpath)))
        booknow_we.click()
        self.logs_obj.info("BOOK NOW button clicked")

