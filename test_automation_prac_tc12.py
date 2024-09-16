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


def test_automation_prac_tc12(driver):
# 2. Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")


# 3. Verify that home page is visible successfully

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(1) > a").text == "Home"
        print("Home page is visible")
    except AssertionError:
        print("Home page is not visible")


# 4. Click 'Products' button
    driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(2) > a").click()


# 5. Hover over first product and click 'Add to cart'
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > .product-image-wrapper > .single-products > .productinfo.text-center > .add-to-cart.btn.btn-default").click()



# 6. Click 'Continue Shopping' button
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-block.btn-success.close-modal").click()


# 7. Hover over second product and click 'Add to cart'
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > .product-image-wrapper > .single-products > .productinfo.text-center > .add-to-cart.btn.btn-default").click()


# 8. Click 'View Cart' button
    driver.find_element(By.CSS_SELECTOR, "u").click()

# 9. Verify both products are added to Cart
    p = driver.find_elements(By.XPATH, "//tr/td[@class='cart_description']/h4")
    product_names = []
    for x in p:
        product_names.append(x.text)

    #print(product_names[0], product_names[1])

    try:
        assert product_names[0] == "Blue Top" and product_names[1] == "Men Tshirt"
        print("both products are added to the cart")
    except AssertionError:
        print("both products are not added to the cart")


# 10. Verify their prices, quantity and total price

    #price
    price = driver.find_elements(By.XPATH, "//tr/td[@class='cart_price']/p")
    price_list = []
    for x in price:
        price_list.append(x.text)

    expected_prices = ["Rs. 500", "Rs. 400"]
    for x in range(len(price_list)):
        try:
            assert price_list[x] == expected_prices[x]
            print("price is matching")
        except AssertionError:
            print("price is not matching")

    # quantity
    quantity = driver.find_elements(By.XPATH, "//tr/td[@class='cart_quantity']/button")
    quantity_list = []
    for x in quantity:
        quantity_list.append(x.text)

    expected_quantity = ["1", "1"]
    for x in range(len(quantity_list)):
        try:
            assert quantity_list[x] == expected_quantity[x]
            print("quantity is matching")
        except AssertionError:
            print("quantity is not matching")

    # total price
    total_price = driver.find_elements(By.XPATH, "//tr/td[@class='cart_total']/p")
    total_price_list = []
    for x in total_price:
        total_price_list.append(x.text)

    expected_total_price_list = ["Rs. 500", "Rs. 400"]
    for x in range(len(total_price_list)):
        try:
            assert total_price_list[x] == expected_total_price_list[x]
            print("Total price is matching")
        except AssertionError:
            print("Total price is not matching")


















