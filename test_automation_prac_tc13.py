import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
# launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
#close browser
    yield driver
    driver.quit()


def test_automation_prac_tc13(driver):
# 2. Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")


# 3. Verify that home page is visible successfully

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(1) > a").text == "Home"
        print("Home page is visible")
    except AssertionError:
        print("Home page is not visible")


# 4. Click 'View Product' for any product on home page
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > .product-image-wrapper > .choose > .nav.nav-justified.nav-pills  a").click()

    time.sleep(5)
# 5. Verify product detail is opened
    prod_name = driver.find_element(By.XPATH, "//div[@class='product-information']/h2").text
    prod_info = driver.find_elements(By.XPATH, "//div[@class='product-information']/p")
    product_details = [prod_name]
    for x in prod_info:
        product_details.append(x.text)

    expected_prod_details = ["Blue Top", "Category: Women > Tops", "Availability: In Stock", "Condition: New", "Brand: Polo"]

    info_titles = ["Product name", "Product category", "Product Availability", "Product Condition", "Product Brand"]
    for x in range(len(product_details)):
        try:
            assert product_details[x] == expected_prod_details[x]
            print(info_titles[x] + " is visible")
        except AssertionError:
            print(info_titles[x] + " is not visible")


# 6. Increase quantity to 4
    qty_box = driver.find_element(By.CSS_SELECTOR, "input#quantity")
    qty_box.clear()
    qty_box.send_keys("4")


# 7. Click 'Add to cart' button
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.cart").click()


# 8. Click 'View Cart' button
    driver.find_element(By.CSS_SELECTOR, "u").click()

# 9. Verify that product is displayed in cart page with exact quantity
    expected_name = "Blue Top"
    expected_quantity = "4"

    try:
        assert driver.find_element(By.XPATH, "//tr/td/h4").text == expected_name and driver.find_element(By.XPATH, "//tr/td/button").text == expected_quantity
        print("product name and quantity is matching")
    except AssertionError:
        print("product name and quantity is not matching")






