from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_utilities.customLogger import logGen
from Test_data import credentials
from Test_locators.test_locators import LoginPageLocators
from time import sleep

class LoginPageActions:
    def __init__(self,driver):
        self.loginpage_obj = LoginPageLocators()
        self.logs_obj = logGen.logger()
        self.driver = driver
        self.driver.get(credentials.url)
        self.driver.maximize_window()
        # self.driver.implicitly_wait(10)

    def enter_username(self):
        """
        find the webelement for username ,clear the text field and set the username passed

        :return:
        """
        username_webelement = self.driver.find_element(By.NAME, self.loginpage_obj.username_loc_txt_name)
        username_webelement.clear()
        username_webelement.send_keys(credentials.username)
        # sleep(5)
        self.logs_obj.info("Username Entered")
        print("Username entered")

    def enter_password(self):
        """
        find the webelement for password ,clear the text field and set the username passed
        :return:
        """
        password_webelement = self.driver.find_element(By.NAME, self.loginpage_obj.password_loc_txt_name)
        password_webelement.clear()
        password_webelement.send_keys(credentials.password)
        # sleep(5)
        self.logs_obj.info("Password Entered")
        print("password entered")

    def click_login(self):
        login_button_webelement = self.driver.find_element(By.XPATH, self.loginpage_obj.login_loc_btn_xpath)
        login_button_webelement.click()
        # sleep(5)
        self.logs_obj.info("Login button clicked")
        print("Login button clicked")

    def login_to_adactin_hotel(self):
        self.enter_username()
        self.enter_password()
        self.click_login()
        self.driver.implicitly_wait(5)
