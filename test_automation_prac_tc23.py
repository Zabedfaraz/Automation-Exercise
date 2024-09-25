import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



# initial info
name = "Ron Wisley"
email = "xxeq@ii"
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






def test_automation_prac_tc23(driver):
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
    country_button.select_by_visible_text(country)
    #state
    driver.find_element(By.CSS_SELECTOR, "input#state").send_keys(state_city)
    #city
    driver.find_element(By.CSS_SELECTOR, "input#city").send_keys(state_city)
    #zip code
    driver.find_element(By.CSS_SELECTOR, "input#zipcode").send_keys(zip_code)
    #Mobile number
    driver.find_element(By.CSS_SELECTOR, "input#mobile_number").send_keys(mobile_number)


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


# 12. Verify that the delivery address is same address filled at the time registration of account

    a = driver.find_elements(By.XPATH, "//div/ul[@class='address item box']/li")
    address_details = []
    for x in a:
        address_details.append(x.text)



    expected_address_details = ["Your delivery address/your billing address", ""'Mr. ' + name, company, address, address2, state_city + " " + state_city + " " + zip_code, country, mobile_number]

    a_failure = 0
    for x in range(len(address_details)):
        if address_details[x] != expected_address_details[x]:
            if x == 0:
                continue
            a_failure += 1

    try:
        assert a_failure == 0
        print("The delivery address is same address filled at the time registration of account")
    except AssertionError:
        print("The delivery address is not the same address filled at the time registration of account")

# 13. Verify that the billing address is same address filled at the time registration of account

    b =  driver.find_elements(By.XPATH, "//div/ul[@class='address alternate_item box']/li")
    billing_address_details = []


    for x in b:
        billing_address_details.append(x.text)


    b_failure = 0
    for x in range(len(address_details)):
        if billing_address_details[x] != expected_address_details[x]:
            if x == 0:
                continue
            b_failure += 1

    try:
        assert b_failure == 0
        print("The billing address is same address filled at the time registration of account")
    except AssertionError:
        print("The billing address is not the same address filled at the time registration of account")



#14. Click 'Delete Account' button
    driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(5) > a").click()



# 15. Verify 'ACCOUNT DELETED!' and click 'Continue' button
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".text-center.title > b").text == "ACCOUNT DELETED!"
        print("Account deleted successfully")
    except AssertionError:
        print("Account deletion failed")
