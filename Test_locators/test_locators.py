class LoginPageLocators:
    def __init__(self):
        pass

    username_loc_txt_name = "username"
    password_loc_txt_name = "password"
    login_loc_btn_xpath = "//input[@name='login']"

class SearchHotelLocators:

    location_loc_dd_xpath = "//select[@name='location']"
    hotels_loc_dd_xpath = "//select[@name='hotels']"
    roomtype_loc_dd_xpath = "//select[@name='room_type']"
    numofrooms_loc_dd_xpath = "//select[@name='room_nos']"
    checkin_loc_txt_xpath = '//input[@name="datepick_in"]'
    checkout_loc_txt_xpath = '//input[@name="datepick_out"]'
    adult_loc_dd_xpath = "//select[@name='adult_room']"
    children_loc_dd_xpath = "//select[@name='child_room']"
    search_loc_btn_xpath = '//input[@name="Submit"]'
    reset_loc_btn_xpath = '//input[@type="reset"]'
    errrormsg_loc_xpath = "//span[text()='Please Select a Location']"

class SelectHotelLocators:

    selecthotel_loc_radio_xpath = '//input[@name="radiobutton_0"]'
    continue_loc_btn_xpath ='//input[@name="continue"]'
    errormsg_select_loc_xpath = "//label[text()='Please Select a Hotel']"

class BookHotelLocators:

    firstname_loc_txt_name = 'first_name'
    lastname_loc_txt_name = 'last_name'
    addr_loc_txt_name = 'address'
    ccnum_loc_txt_name = 'cc_num'
    cctype_loc_dd_xpath = "//select[@name='cc_type']"
    expmonth_loc_dd_xpath = "//select[@name='cc_exp_month']"
    expyear_loc_dd_xpath = "//select[@name='cc_exp_year']"
    # cvv_loc_txt_xpath = "//input[@name='cc_cvv']"
    cvv_loc_txt_id = 'username_show'
    booknow_loc_btn_xpath = "//input[@name='book_now']"