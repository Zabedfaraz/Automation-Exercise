import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



name = "Ron Wisley"
email = "ronwisley12345432@gmail.com"
password = "121212"

@pytest.fixture
def driver():
# launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
#close browser
    yield driver
    driver.quit()


def test_automation_prac_tc21(driver):
# 2. Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")


# 3. Click on 'Products' button
    driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(2) > a").click()


# 4. Verify user is navigated to ALL PRODUCTS page successfully

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".text-center.title").text == "ALL PRODUCTS"
        print("Navigated to All products page successfully")
    except AssertionError:
        print("Failed to navigate to All products page")


# 5. Click on 'View Product' button
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > .product-image-wrapper > .choose > .nav.nav-justified.nav-pills  a").click()

# 6. Verify 'Write Your Review' is visible
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".nav.nav-tabs  a").text == "WRITE YOUR REVIEW"
        print("'Write your review' is visible")
    except AssertionError:
        print("'Write your review' is not visible")


# 7. Enter name, email and review
    driver.find_element(By.CSS_SELECTOR, "input#name").send_keys("Zabed")
    driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("Z@W")
    driver.find_element(By.CSS_SELECTOR, "textarea#review").send_keys("Good product")


# 8. Click 'Submit' button
    driver.find_element(By.CSS_SELECTOR, "button#button-review").click()


# 9. Verify success message 'Thank you for your review.'
    try:
        assert driver.find_element(By.XPATH, "//div[@class='alert-success alert']/span").text == "Thank you for your review."
        print("Review success message is visible")
    except AssertionError:
        print("Review success message is not visible")


