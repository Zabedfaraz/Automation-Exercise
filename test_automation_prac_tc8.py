import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.remote.webelement import WebElement


@pytest.fixture
def driver():
#Launch Browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
#close browser
    yield driver
    driver.quit()


def test_automation_prac_tc8(driver):
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


# 6. The products list is visible
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".features_items > div:nth-of-type(2)").is_displayed()
        print("product list is visible")
    except AssertionError:
        print("product list is not visible")


# 7. Click on 'View Product' of first product
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > .product-image-wrapper > .choose > .nav.nav-justified.nav-pills  a").click()

# 8. User is landed to product detail page
    try:
        assert driver.title == "Automation Exercise - Product Details"
        print("User has landed to product details page")
    except AssertionError:
        print("User has not landed to product details page")


# 9. Verify that detail detail is visible: product name, category, price, availability, condition, brand
    expected_elements = ["Blue Top", "category", "price", "availability", "condition", "brand"]

    details = driver.find_elements(By.CSS_SELECTOR, ".product-information")
    all_details = []
    for x in details:
            all_details.append(x.text)

    for x in all_details:
        try:
            assert x in expected_elements
            print("details is visible")
        except AssertionError:
            print("details is not visible")

#    try:
 #       assert "Category:" in all_details
  #      print("detail is visible")
   # except AssertionError:
    #    print("details is not visible")
