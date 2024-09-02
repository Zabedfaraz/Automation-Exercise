import time
import pytest
import selenium.webdriver.support.select
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By

# initial info
name = "Ron Wisley"
email = "ronwisley12345432@gmail.com"
password = "121212"
company = "People and Tech"
address = "223/B, baker Street, East London"
address2 = "44/6, new york, USA"


@pytest.fixture
# 1. Launch browser
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
#close browser
    yield driver
    driver.quit()

def test_automation_prac_tc5(driver):
# 2. Navigate to URL
    driver.get('http://automationexercise.com')


# 3. Verify that home page is visible successfully

    try:
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



# 6. Enter name and already registered email address
    driver.find_element(By.CSS_SELECTOR, "form[method='post'] > input[name='name']").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > input[name='email']").send_keys(email)


# 7. Click 'Signup' button
    driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > .btn.btn-default").click()


# 8. Verify error 'Email Address already exist!' is visible

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".signup-form > form[method='post'] > p").text == "Email Address already exist!"
        print("'Email Address already exist!' message is visible")
    except AssertionError:
        print("'Email Address already exist!' message is not visible")
