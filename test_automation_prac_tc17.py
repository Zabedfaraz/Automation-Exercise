import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


name = "Ron Wisley"
email = "qq@mm"
password = "121212"
company = "People and Tech"
address = "223/B, baker Street, East London"
address2 = "44/6, new york, USA"




@pytest.fixture
def driver():
# launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
#close browser
    yield driver
    driver.quit()


def test_automation_prac_tc17(driver):
# 2. Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")


# 3. Verify that home page is visible successfully

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(1) > a").text == "Home"
        print("Home page is visible")
    except AssertionError:
        print("Home page is not visible")


# 4. Add products to cart
    req_items = ["Blue Top", "Men Tshirt"]
    available_products = driver.find_elements(By.XPATH, "//div[@class='features_items']//div[@class='productinfo text-center']//p")
    add_cart_button = driver.find_elements(By.XPATH, "//div[@class='features_items']//div[@class='productinfo text-center']//a")

    for x in range(len(req_items)):
        if available_products[x].text == req_items[x]:
            add_cart_button[x].click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, ".btn.btn-block.btn-success.close-modal").click()

# 5. Click 'Cart' button
    driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(3) > a").click()


# 6. Verify that cart page is displayed
    try:
        assert driver.title == "Automation Exercise - Checkout"
        print("Cart page is displayed")
    except AssertionError:
        print("Cart page is not displayed")

# 7. Click 'X' button corresponding to particular product
    # variables required for the operation
    name_box = driver.find_elements(By.XPATH, "//table/tbody/tr/td/h4")
    expected_name = "Blue Top"
    delete_buttons = driver.find_elements(By.XPATH, "//tr/td[@class='cart_delete']/a[@class='cart_quantity_delete']")
    products = driver.find_elements(By.XPATH, "//div/table/tbody/tr")

    # deleting blue top item
    for x in range(len(products)):
        if name_box[x].text == expected_name:
            delete_buttons[x].click()




