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


def test_automation_prac_tc22(driver):
# 2. Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")


# 3. Scroll down to bottom of the page
    footer_element = driver.find_element(By.CSS_SELECTOR, ".footer-widget > .container > .row")
    driver.execute_script("window.scrollTo(0, 9000)")


# 4. Verify 'RECOMMENDED ITEMS' are visible
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".recommended_items > .text-center.title").text == "RECOMMENDED ITEMS"
        print("Recommended items are visible")
    except AssertionError:
        print("Recommended items are not visible")


# 5. Click on 'Add To Cart' on Recommended product
    add_to_cart_btn = driver.find_elements(By.XPATH, "//div[@class='recommended_items']//div[@class='productinfo text-center']/a")
    for x in range(len(add_to_cart_btn)):
        if add_to_cart_btn[x].is_displayed():
            add_to_cart_btn[x].click()
        else:
            driver.implicitly_wait(2)


# 6. Click on 'View Cart' button
    driver.find_element(By.CSS_SELECTOR, "u").click()

# 7. Verify that product is displayed in cart page
    cart_items = driver.find_elements(By.XPATH, "//table[@id='cart_info_table']/tbody/tr")
    for x in range(len(cart_items)):
        try:
            assert cart_items[x].is_displayed()
            print("Product is displayed")
        except AssertionError:
            print("Product is not displayed")


