import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
# launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
#close browser
    yield driver
    driver.quit()


def test_automation_prac_tc11(driver):
# 2. Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")


# 3. Verify that home page is visible successfully

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(1) > a").text == "Home"
        print("Home page is visible")
    except AssertionError:
        print("Home page is not visible")


# 4. Click 'Cart' button
    driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(3) > a").click()


# 5. Scroll down to footer
    driver.execute_script("window.scrollTo(0, 5000)")



# 6. Verify text 'SUBSCRIPTION'
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".footer-widget > .container h2").text == "SUBSCRIPTION"
        print("Subscription text is visible")
    except AssertionError:
        print("Subscription text is not visible")


# 7. Enter email address in input and click arrow button
    driver.find_element(By.CSS_SELECTOR, "input#susbscribe_email").send_keys("wow@mail.com")
    driver.find_element(By.CSS_SELECTOR, "button#subscribe > .fa.fa-arrow-circle-o-right").click()



# 8. Verify success message 'You have been successfully subscribed!' is visible

