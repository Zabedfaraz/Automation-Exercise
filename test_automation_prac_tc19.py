import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select






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




# 4. Verify that Brands are visible on left side bar
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".brands_products > h2").text == "BRANDS"
        print("Brands are visible")
    except AssertionError:
        print("Brands are not visible")


# 5. Click on any brand name
    brs = driver.find_elements(By.XPATH, "//ul[@class='nav nav-pills nav-stacked']/li/a")
    brands = []
    for x in range(len(brs)):
        brands.append(brs[x].text.split("\n")[1])

    req_brand = ["POLO", "H&M", "MADAME"]

    for x in range(len(req_brand)):
        if req_brand[0] == brands[x]:
            brs[x].click()

 #   time.sleep(5)

# 6. Verify that user is navigated to brand page and brand products are displayed
    print(driver.find_element(By.CSS_SELECTOR, ".text-center.title").text)
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".text-center.title").text == "BRAND -  POLO PRODUCTS"
        print("Navigated to brand products page successfully")
    except AssertionError:
        print("Failed to navigate to brand products")



# 7. On left side bar, click on any other brand link
    time.sleep(5)
    brs1 = driver.find_elements(By.XPATH, "//ul[@class='nav nav-pills nav-stacked']/li/a")
    for x in range(len(req_brand)):
        if req_brand[1] == brands[x]:
            brs1[x].click()


# 8. Verify that user is navigated to that brand page and can see products
    print(driver.find_element(By.CSS_SELECTOR, ".text-center.title").text)
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".text-center.title").text == "BRAND - H&M PRODUCTS"
        print("Navigated to brand products page successfully")
    except AssertionError:
        print("Failed to navigate to brand products")