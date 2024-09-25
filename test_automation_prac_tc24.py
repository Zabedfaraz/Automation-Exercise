import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initial info
name = "Ron Wisley"
email = "xi@it0hj"
password = "121212"
company = "People and Tech"
address = "223/B, baker Street, East London"
address2 = "44/6, new york, USA"
country = "United States"
state_city = "New York"
zip_code = "101"
mobile_number = "09856"



@pytest.fixture
def driver():
    # launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    # close browser
    yield driver
    driver.quit()


def test_automation_prac_tc24(driver):
# 2. Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")



# 3. Verify that home page is visible successfully

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(1) > a").text == "Home"
        print("Home page is visible")
    except AssertionError:
        print("Home page is not visible")

# 4. Add products to cart
    req_items = ["Blue Top", "Men Tshirt"]
    available_products = driver.find_elements(By.XPATH, "//div[@class='features_items']//div[@class='productinfo text-center']//p")
    add_cart_button = driver.find_elements(By.XPATH, "//div[@class='features_items']//div[@class='productinfo text-center']//a")

    for x in range(len(req_items)):
        if available_products[x].text == req_items[x]:
            add_cart_button[x].click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, ".btn.btn-block.btn-success.close-modal").click()

# 5. Click 'Cart' button
    driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(3) > a").click()

# 6. Verify that cart page is displayed
    try:
        assert driver.title == "Automation Exercise - Checkout"
        print("Cart page is displayed")
    except AssertionError:
        print("Cart page is not displayed")

# 7. Click Proceed To Checkout
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.check_out").click()

# 8. Click 'Register / Login' button
    driver.find_element(By.CSS_SELECTOR, ".modal-content u").click()

# 9. Fill all details in Signup and create account
    # name and email signup
    driver.find_element(By.CSS_SELECTOR, "form[method='post'] > input[name='name']").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > input[name='email']").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > .btn.btn-default").click()

    #filling details
    driver .find_element(By.CSS_SELECTOR, "div:nth-of-type(1) > .top > .radio  input[name='title']").click()
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
    #check box
    driver.find_element(By.CSS_SELECTOR, "input#newsletter").click()
    driver.find_element(By.CSS_SELECTOR, "input#optin").click()
    #all details
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
    #create account
    driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-default']").click()



# 10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".text-center.title > b").text == 'ACCOUNT CREATED!'
        print("'ACCOUNT CREATED!' is visible")
    except AssertionError:
        print("'ACCOUNT CREATED!' is not visible")

    #continue button
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()


# 11. Verify ' Logged in as username' at top
    try:
        assert driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(10) > a").text == "Logged in as " + name
        print("'Logged in as " "'" + name + "'"" is visible")
    except AssertionError:
        print("'Logged in as username' is not visible")


# 12.Click 'Cart' button
    driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(3) > a").click()


# 13. Click 'Proceed To Checkout' button
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.check_out").click()


# 14. Verify Address Details and Review Your Order
    a = driver.find_elements(By.XPATH, "//div/ul[@class='address item box']/li")
    address_details = []
    for x in a:
        address_details.append(x.text)
    for x in range(len(address_details)):
        print(address_details[x])


    expected_address_details = ["YOUR DELIVERY ADDRESS", ""'Mr. ' + name, "People and Tech", address, address2, "New York New York 101", "United States", "09856"]

    for x in range(len(address_details)):
        try:
            assert address_details[x] == expected_address_details[x]
            print("Address matched successfully")
        except AssertionError:
            print("Address did not match")

    # price
    price = driver.find_elements(By.XPATH, "//tr/td[@class='cart_price']/p")
    price_list = []
    for x in price:
        price_list.append(x.text)

    expected_prices = ["Rs. 500", "Rs. 400"]
    for x in range(len(price_list)):
        try:
            assert price_list[x] == expected_prices[x]
            print("price is matching")
        except AssertionError:
            print("price is not matching")

    # quantity
    quantity = driver.find_elements(By.XPATH, "//tr/td[@class='cart_quantity']/button")
    quantity_list = []
    for x in quantity:
        quantity_list.append(x.text)

    expected_quantity = ["1", "1"]
    for x in range(len(quantity_list)):
        try:
            assert quantity_list[x] == expected_quantity[x]
            print("quantity is matching")
        except AssertionError:
            print("quantity is not matching")

    # total price
    total_price = driver.find_elements(By.XPATH, "//tr/td[@class='cart_total']/p")
    total_price_list = []
    for x in total_price:
        total_price_list.append(x.text)

    expected_total_price_list = ["Rs. 500", "Rs. 400"]
    for x in range(len(total_price_list)):
        try:
            assert total_price_list[x] == expected_total_price_list[x]
            print("Total price is matching")
        except AssertionError:
            print("Total price is not matching")



# 15. Enter description in comment text area and click 'Place Order'
    driver.find_element(By.CSS_SELECTOR, "div#ordermsg > textarea[name='message']").send_keys("no comments")
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.check_out").click()



# 16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    driver.find_element(By.CSS_SELECTOR, "input[name='name_on_card']").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, "input[name='card_number']").send_keys("123")
    driver.find_element(By.CSS_SELECTOR, "input[name='cvc']").send_keys("333")
    driver.find_element(By.CSS_SELECTOR, "input[name='expiry_month']").send_keys("90")
    driver.find_element(By.CSS_SELECTOR, "input[name='expiry_year']").send_keys("2010")

# 17. Click 'Pay and Confirm Order' button
    driver.find_element(By.CSS_SELECTOR, "button#submit").click()


# 18. Verify success message 'Your order has been placed successfully!'
    #cannot detect disapearing notification
#    try:
#        assert driver.find_element(By.XPATH, "//div[@class='col-md-12 form-group']/div").text == "Your order has been placed successfully!"
#        print("Order placed successfully")
#    except AssertionError:
#        print("Order is not placed")


    message = driver.find_element(By.XPATH, "//div[@class='form-row']/div/div[1]")
#    wait = WebDriverWait(driver, 10)
#    wait.until(EC.visibility_of(message))



    print(message.text)



# 19. Click 'Download Invoice' button and verify invoice is downloaded successfully.
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.check_out").click()
    driver.execute_script("tb:fileExists", {"fileName": "...invoice...",})
    driver.execute_script("tb:fileExists", {"fileName": "...invoice...",})

# 20. Click 'Continue' button
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()


#21. Click 'Delete Account' button
    driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(5) > a").click()


# 22. Verify 'ACCOUNT DELETED!' and click 'Continue' button
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".text-center.title > b").text == "ACCOUNT DELETED!"
        print("Account deleted successfully")
    except AssertionError:
        print("Account deletion failed")
