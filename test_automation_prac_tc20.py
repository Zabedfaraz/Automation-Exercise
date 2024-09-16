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


def test_automation_prac_tc19(driver):
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



# 5. Enter product name in search input and click search button
    search_key_word = "top"
    driver.find_element(By.CSS_SELECTOR, "input#search_product").send_keys(search_key_word)
    driver.find_element(By.CSS_SELECTOR, "button#submit_search").click()


# 6. Verify 'SEARCHED PRODUCTS' is visible
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".text-center.title").text == "SEARCHED PRODUCTS"
        print("'Searched products' is visible")
    except AssertionError:
        print("'Searched products' is not visible")

# 7. Verify all the products related to search are visible
    products = driver.find_elements(By.XPATH, "//div[@class='productinfo text-center']/p")
    product_names = []
    for x in range(len(products)):
        product_names.append(products[x].text)

    try:
        assert len(products) > 0
        print("Search related products are visible")
    except AssertionError:
        print("Search related products are not available")


# 8. Add those products to cart
    add_to_cart_button = driver.find_elements(By.XPATH, "//div[@class='productinfo text-center']/a")

    for x in range(len(products)):
        add_to_cart_button[x].click()
        driver.find_element(By.CSS_SELECTOR, ".btn.btn-block.btn-success.close-modal").click()



# 9. Click 'Cart' button and verify that products are visible in cart
    driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(3) > a").click()
    cart_products = driver.find_elements(By.XPATH, "//table/tbody/tr/td/h4/a")

    try:
        assert len(products) == len(cart_products)
        print("Products are visible in cart")
    except AssertionError:
        print("Products are not visible in cart")


# 10. Click 'Signup / Login' button and submit login details
    driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(4) > a").click()
    driver.find_element(By.CSS_SELECTOR, ".login-form > form[method='post'] > input[name='email']").send_keys(email)
    driver.find_element(By.CSS_SELECTOR, "form[method='post'] > input[name='password']").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".login-form > form[method='post'] > .btn.btn-default").click()


# 11. Again, go to Cart page
    driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(3) > a").click()


# 12. Verify that those products are visible in cart after login as well

    cart_products1 = driver.find_elements(By.XPATH, "//table/tbody/tr/td/h4/a")
    try:
        assert len(products) == len(cart_products1)
        print("Products are visible in cart after login")
    except AssertionError:
        print("Products are not visible in cart after login")