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


def test_automation_prac_tc25(driver):
# 2. Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")


# 3. Verify that home page is visible successfully

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(1) > a").text == "Home"
        print("Home page is visible")
    except AssertionError:
        print("Home page is not visible")


# 4. Scroll down page to bottom
    footer_element = driver.find_element(By.CSS_SELECTOR, ".footer-widget > .container > .row")
    driver.execute_script("window.scrollTo(0, 9000)")


# 5. Verify text 'SUBSCRIPTION' is visible
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".footer-widget > .container h2").text == "SUBSCRIPTION"
        print("Subscription text is visible")
    except AssertionError:
        print("Subscription text is not visible")


# 6. Click on arrow at bottom right side to move upward
    driver.find_element(By.CSS_SELECTOR, "a#scrollUp > .fa.fa-angle-up").click()

    time.sleep(10)

# 7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
    try:
        assert driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > div:nth-of-type(1) > h2").text == "Full-Fledged practice website for Automation Engineers"
        print("Required text is visible")
    except AssertionError:
        print("Required text is not visible")

    print(driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > div:nth-of-type(1) > h2").text)