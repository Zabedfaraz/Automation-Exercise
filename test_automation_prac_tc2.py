import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
from selenium.webdriver.support.ui import Select



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

def test_automation_prac_tc2(driver):
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


# 5. Verify 'Login to your account' is visible
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".login-form > h2").text == "Login to your account"
        print("'Login to your account' is visible")
    except AssertionError:
        print("'Login to your account' is not visible")


# 6. Enter correct email address and password
    driver.find_element(By.CSS_SELECTOR, ".login-form > form[method='post'] > input[name='email']").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "form[method='post'] > input[name='password']").send_keys(password)


# 7. Click 'login' button
    driver.find_element(By.CSS_SELECTOR, ".login-form > form[method='post'] > .btn.btn-default").click()


# 8. Verify that 'Logged in as username' is visible
    try:
        assert driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(10) > a").text == "Logged in as " + name
        print("'Logged in as " "'" + name + "'"" is visible")
    except AssertionError:
        print("'Logged in as username' is not visible")
# 9. Click 'Delete Account' button
    #driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(5) > a").click()


# 10. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    #try:
    #    assert driver.find_element(By.CSS_SELECTOR, ".text-center.title > b").text == 'ACCOUNT DELETED!'
     #   print("'ACCOUNT DELETED!' is visible")
    #except AssertionError:
     #   print("'ACCOUNT DELETED!' is not visible")

