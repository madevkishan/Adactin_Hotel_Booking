# Adactin_Hotel_Booking

Testscases dealing with Adactin Hotel Booking
=============================================

1. test_login_page_title  = Successful User Login to Adactin Hotel Booking

2. test_search_hotel_page_positive = User provides valid inputs in 'Search Hotel' page and can move on to next page without any issues

3. test_search_hotel_page_negative_1 = without providing inputs user tried to move on to next page

4. test_search_hotel_page_negative_2 = User tried to provide invalid inputs

5. test_select_hotel_page_positive = User can succuessfully 'select hotel' and move on to next page

6. test_select_hotel_page_negative_1 = without selecting the hotel,user cannot move on to next page

7. test_book_hotel_page_positive = User could book the hotels


PageObjects = For each Page,A CLASS has been created which contains the functions/tasks to be performed on that page 

Locators = To perform action on the webelements,we need to locate the webelements and they are defined in a separate class file,so it would be easy to maintain the code

Logs = As automation is a quick operation,it will be difficult for us to see what's opening,so its better to log our operations for better understanding 

Screenshots = Its a good practice to capture the screenshot of failed testcases.

Test data = It contains the common data which are to be used all over the testcases.

Test cases = Each testcase contains only the logic.

Though it's not recommended to use implicit wait,I have used it show the input we insert into each field.
Please check automation.log also

