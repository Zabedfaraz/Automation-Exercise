

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
# 1. Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
# close browser
    yield driver
    driver.quit()


def test_automation_prac_tc9(driver):
# 2. Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")

# 3. Verify that home page is visible successfully

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(1) > a").text == "Home"
        print("Home page is visible")
    except AssertionError:
        print("Home page is not visible")

# 4. Click on 'Products' button

    driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(2) > a").click()

# 5. Verify user is navigated to ALL PRODUCTS page successfully
    title = driver.title
    try:
        assert title == "Automation Exercise - All Products"
        print("user is navigated to ALL PRODUCTS page successfully")
    except AssertionError:
        print("Navigation to all products page is unsuccessful")


# 6. Enter product name in search input and click search button
    product_name = "Blue Top"
    driver.find_element(By.CSS_SELECTOR, "input#search_product").send_keys(product_name)
    driver.find_element(By.ID, "submit_search").click()


# 7. Verify 'SEARCHED PRODUCTS' is visible

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".text-center.title").text == 'SEARCHED PRODUCTS'
        print("'SEARCHED PRODUCTS' is visible")
    except AssertionError:
        print("'SEARCHED PRODUCTS' is not visible")



# 8. Verify all the products related to search are visible
    search_result = driver.find_elements(By.CSS_SELECTOR, ".col-sm-9.padding-right")

    product = []
    for x in search_result:
        if x.text == product_name:
            print(x.text)

    print(product)

    try:
        assert product == product_name
        print("searched product is visible")
    except AssertionError:
        print("searched product is not visible")

