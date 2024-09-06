import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture
def driver():
#Launch Browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
#close browser
    yield driver
    driver.quit()


def test_automation_prac_tc7(driver):
# 2. Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")


# 3. Verify that home page is visible successfully

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(1) > a").text == "Home"
        print("Home page is visible")
    except AssertionError:
        print("Home page is not visible")

# 4. Click on 'Test Cases' button

    driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(5) > a").click()


# 5. Verify user is navigated to test cases page successfully

    try:
        assert driver.find_element(By.CSS_SELECTOR, "b").text == "TEST CASES"
        print("Navigation to test case page is successful")
    except AssertionError:
        print("Navigation to test case page is unsuccessful")

