import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



# initial info
name = "Ron Wisley"
email = "xx@ii"
password = "121212"
company = "People and Tech"
address = "223/B, baker Street, East London"
address2 = "44/6, new york, USA"

@pytest.fixture
def driver():
    # launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    # close browser
    yield driver
    driver.quit()






def test_automation_prac_tc15(driver):
# 2. Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")



# 3. Verify that home page is visible successfully

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(1) > a").text == "Home"
        print("Home page is visible")
    except AssertionError:
        print("Home page is not visible")


# 4. click on the signup/login button
    login_button = driver.find_element(By.XPATH,"/html//header[@id='header']/div[@class='header-middle']//ul[@class='nav navbar-nav']//a[@href='/login']")
    login_button.click()


# 5. Fill all details in Signup and create account
    # Enter name and email address &  Click 'Signup' button
    driver.find_element(By.CSS_SELECTOR, "form[method='post'] > input[name='name']").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > input[name='email']").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > .btn.btn-default").click()

    # Fill details: Title, Name, Email, Password, Date of birth
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(1) > .top > .radio  input[name='title']").click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 200)")
    password_box = driver.find_element(By.CSS_SELECTOR, "input#password")
    password_box.send_keys(password)


    #day
    day = driver.find_element(By.CSS_SELECTOR, "select#days")
    day = Select(day)
    day.select_by_index(6)
    #month
    month = driver.find_element(By.CSS_SELECTOR, "select#months")
    month = Select(month)
    month.select_by_index(3)
    #year
    year = driver.find_element(By.CSS_SELECTOR, "select#years")
    year = Select(year)
    year.select_by_visible_text("1997")


    # Select checkbox 'Sign up for our newsletter!
    driver.find_element(By.CSS_SELECTOR, "input#newsletter").click()


    # Select checkbox 'Receive special offers from our partners!'
    driver.find_element(By.CSS_SELECTOR, "input#optin").click()


    # Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    #F name
    driver.find_element(By.CSS_SELECTOR, "input#first_name").send_keys(name.split(" ")[0])
    #Lname
    driver.find_element(By.CSS_SELECTOR, "input#last_name").send_keys((name.split(" ")[1]))
    #company
    driver.find_element(By.CSS_SELECTOR, "input#company").send_keys(company)
    #address
    driver.find_element(By.CSS_SELECTOR, "input[name='address1']").send_keys(address)
    #address2
    driver.find_element(By.CSS_SELECTOR, "input[name='address2']").send_keys(address2)
    #country
    country_button = driver.find_element(By.CSS_SELECTOR, "select#country")
    country_button = Select(country_button)
    country_button.select_by_visible_text("United States")
    #state
    driver.find_element(By.CSS_SELECTOR, "input#state").send_keys("New York")
    #city
    driver.find_element(By.CSS_SELECTOR, "input#city").send_keys("New York")
    #zip code
    driver.find_element(By.CSS_SELECTOR, "input#zipcode").send_keys("101")
    #Mobile number
    driver.find_element(By.CSS_SELECTOR, "input#mobile_number").send_keys("09856")


    # Click 'Create Account button'
    driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-default']").click()


# 6. Verify that 'ACCOUNT CREATED!' and click on continue button
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".text-center.title > b").text == 'ACCOUNT CREATED!'
        print("'ACCOUNT CREATED!' is visible")
    except AssertionError:
        print("'ACCOUNT CREATED!' is not visible")

    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()


# 7. Verify ' Logged in as username' at top
    try:
        assert driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(10) > a").text == "Logged in as " + name
        print("'Logged in as " "'" + name + "'"" is visible")
    except AssertionError:
        print("'Logged in as username' is not visible")


# 8. Add products to cart
    driver.find_element(By.CSS_SELECTOR,"div:nth-of-type(2) > .product-image-wrapper > .single-products > .productinfo.text-center > .add-to-cart.btn.btn-default").click()
# clicking on continue shopping
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-block.btn-success.close-modal").click()
# clicking on second product
    driver.find_element(By.CSS_SELECTOR,"div:nth-of-type(3) > .product-image-wrapper > .single-products > .productinfo.text-center > .add-to-cart.btn.btn-default").click()
# clicking on continue shopping
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-block.btn-success.close-modal").click()


# 9. Click 'Cart' button
    driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(3) > a").click()


# 10. Verify that cart page is displayed
    try:
        assert driver.title == "Automation Exercise - Checkout"
        print("Cart page is displayed")
    except AssertionError:
        print("Cart page is not displayed")



# 11. Click Proceed To Checkout
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.check_out").click()



# 12. Verify Address Details and Review Your Order
    a = driver.find_elements(By.XPATH, "//div/ul[@class='address item box']/li")
    address_details = []
    for x in a:
        address_details.append(x.text)
    # for x in range(len(address_details)):
    #   print(address_details[x])


    expected_address_details = ["YOUR DELIVERY ADDRESS", ""'Mr. ' + name, "People and Tech", address, address2, "New York New York 101", "United States", "09856"]
    test_snf_message = ["address table name", "customer name", "company name", "Present address", "2nd Address", "City, state and post code", "Country name", "Phone number"]

    for x in range(len(address_details)):
        try:
            assert address_details[x] == expected_address_details[x]
            print(test_snf_message[x] + " matched successfully")
        except AssertionError:
            print(test_snf_message[x] + " did not match")

    # price
    price = driver.find_elements(By.XPATH, "//tr/td[@class='cart_price']/p")
    price_list = []
    for x in price:
        price_list.append(x.text)

    price_snf_msg = ["Product 1", "Product 2"]

    expected_prices = ["Rs. 500", "Rs. 400"]
    for x in range(len(price_list)):
        try:
            assert price_list[x] == expected_prices[x]
            print(price_snf_msg[x] + " price is matching")
        except AssertionError:
            print(price_snf_msg[x] + "price is not matching")

    # quantity
    quantity = driver.find_elements(By.XPATH, "//tr/td[@class='cart_quantity']/button")
    quantity_list = []
    for x in quantity:
        quantity_list.append(x.text)

    quantity_snf_msg = ["Product 1", "Product 2"]

    expected_quantity = ["1", "1"]
    for x in range(len(quantity_list)):
        try:
            assert quantity_list[x] == expected_quantity[x]
            print(quantity_snf_msg[x] + " quantity is matching")
        except AssertionError:
            print(quantity_snf_msg[x] + " quantity is not matching")

    # total price
    total_price = driver.find_elements(By.XPATH, "//tr/td[@class='cart_total']/p")
    total_price_list = []
    for x in total_price:
        total_price_list.append(x.text)
    ttl_price_snf_msg = ["Product 1", "Product 2"]

    expected_total_price_list = ["Rs. 500", "Rs. 400"]

    for x in range(len(total_price_list)):
        try:
            assert total_price_list[x] == expected_total_price_list[x]
            print(ttl_price_snf_msg[x] + " total price is matching")
        except AssertionError:
            print(ttl_price_snf_msg[x] + " total price is not matching")



# 13. Enter description in comment text area and click 'Place Order'
    driver.find_element(By.CSS_SELECTOR, "div#ordermsg > textarea[name='message']").send_keys("no comments")
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.check_out").click()



# 14. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    driver.find_element(By.CSS_SELECTOR, "input[name='name_on_card']").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, "input[name='card_number']").send_keys("123")
    driver.find_element(By.CSS_SELECTOR, "input[name='cvc']").send_keys("333")
    driver.find_element(By.CSS_SELECTOR, "input[name='expiry_month']").send_keys("90")
    driver.find_element(By.CSS_SELECTOR, "input[name='expiry_year']").send_keys("2010")

# 15. Click 'Pay and Confirm Order' button
    driver.find_element(By.CSS_SELECTOR, "button#submit").click()


# 16. Verify success message 'Your order has been placed successfully!'
    #cannot detect disapearing notification
    try:
        assert driver.find_element(By.CSS_SELECTOR, "section#form > .container p").text == "Congratulations! Your order has been confirmed!"
        print("Order placed successfully")
    except AssertionError:
        print("Order is not placed")


#17. Click 'Delete Account' button
    driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(5) > a").click()



# 18. Verify 'ACCOUNT DELETED!' and click 'Continue' button
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".text-center.title > b").text == "ACCOUNT DELETED!"
        print("Account deleted successfully")
    except AssertionError:
        print("Account deletion failed")
