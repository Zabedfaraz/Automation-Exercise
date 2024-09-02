import pytest
import time

import selenium.webdriver.support.select
from select import select
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.ui import Select
from pynput.keyboard import Key, Controller

# initial info
name = "Ron Wisley"
email = "riyak8584333@avashost.com"
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
# close browser
    yield driver
    driver.quit()


def test_automation_prac_tc6(driver):
# 2. Navigate to URL
    driver.get('http://automationexercise.com')


# 3. Verify that home page is visible successfully

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(1) > a").text == "Home"
        print("Home page is visible")
    except AssertionError:
        print("Home page is not visible")


# 4. Click on 'Contact Us' button
    driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(8) > a").click()


# 5. Verify 'GET IN TOUCH' is visible

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".contact-form > .text-center.title").text == "GET IN TOUCH"
        print("'GET IN TOUCH' is visible")
    except AssertionError:
        print("'GET IN TOUCH' is not visible")


# 6. Enter name, email, subject and message
    driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "input[name='subject']").send_keys("query")
    driver.find_element(By.CSS_SELECTOR, "textarea#message").send_keys("hello")
    time.sleep(3)


# 7. Upload file
    upload_button = driver.find_element(By.CSS_SELECTOR, "[name='upload_file']")
    upload_button.send_keys("C:\\Users\\HP\\Desktop\\P2.png")



# 8. Click 'Submit' button
    driver.find_element(By.CSS_SELECTOR, "input[name='submit']").click()


# 9. Click OK button
    driver.switch_to.alert.accept()


# 10. Verify success message 'Success! Your details have been submitted successfully.' is visible

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.status").text == "Success! Your details have been submitted successfully."
        print("'Success! Your details have been submitted successfully.' is visible")
    except AssertionError:
        print("'Success! Your details have been submitted successfully.' is not visible")




# 11. Click 'Home' button and verify that landed to home page successfully
    driver.find_element(By.CSS_SELECTOR, "span").click()

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(1) > a").text == "Home"
        print("Home page is visible")
    except AssertionError:
        print("Home page is not visible")

