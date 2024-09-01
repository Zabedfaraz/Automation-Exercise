import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.ui import Select
import random
import string

def generate_random_email():
    domain = "@example.com"
    username_length = random.randint(5, 10)
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(username_length))
    return username + domain


# initial info
name = "Ron Wisley"
email = generate_random_email()
password = "121212"
company = "People and Tech"
address = "223/B, baker Street, East London"
address2 = "44/6, new york, USA"


@pytest.fixture
def driver():
    # 1. Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    # close browser
    yield driver
    driver.quit()

def test_automation_prac_tc1(driver):
    # 2. Navigate to URL
    driver.get('http://automationexercise.com')
    try:
        # 3. Verify that home page is visible successfully
        assert driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(1) > a").text == "Home"
        print("Home page is visible")
    except AssertionError:
        print("Home page is not visible")


# 4. click on the signup/login button
    login_button = driver.find_element(By.XPATH,"/html//header[@id='header']/div[@class='header-middle']//ul[@class='nav navbar-nav']//a[@href='/login']")
    login_button.click()


# 5. Verify 'New User Signup!' is visible
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".signup-form > h2").text == "New User Signup!"
        print("New user sign up message is visible")
    except AssertionError:
        print("New user sign up message is not visible")

# 6. Enter name and email address & 7. Click 'Signup' button
    driver.find_element(By.CSS_SELECTOR, "form[method='post'] > input[name='name']").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > input[name='email']").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > .btn.btn-default").click()


# 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".login-form > .text-center.title > b").text == "ENTER ACCOUNT INFORMATION"
        print("'ENTER ACCOUNT INFORMATION' is visible")
    except AssertionError:
        print("'ENTER ACCOUNT INFORMATION' is not visible")


# 9. Fill details: Title, Name, Email, Password, Date of birth
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


# 10. Select checkbox 'Sign up for our newsletter!
    driver.find_element(By.CSS_SELECTOR, "input#newsletter").click()


# 11. Select checkbox 'Receive special offers from our partners!'
    driver.find_element(By.CSS_SELECTOR, "input#optin").click()


# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
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


# 13. Click 'Create Account button'
    driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-default']").click()


# 14. Verify that 'ACCOUNT CREATED!' is visible
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".text-center.title > b").text == 'ACCOUNT CREATED!'
        print("'ACCOUNT CREATED!' is visible")
    except AssertionError:
        print("'ACCOUNT CREATED!' is not visible")


# 15. Click 'Continue' button
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()


# 16. Verify that 'Logged in as username' is visible
    try:
        assert driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(10) > a").text == "Logged in as " + name
        print("'Logged in as " "'" + name + "'"" is visible")
    except AssertionError:
        print("'Logged in as username' is not visible")


# 17. Click 'Delete Account' button
    driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(5) > a").click()


# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".text-center.title > b").text == 'ACCOUNT DELETED!'
        print("'ACCOUNT DELETED!' is visible")
    except AssertionError:
        print("'ACCOUNT DELETED!' is not visible")
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()





