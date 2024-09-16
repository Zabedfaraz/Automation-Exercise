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


def test_automation_prac_tc18(driver):
# 2. Navigate to url 'http://automationexercise.com'
    driver.get("http://automationexercise.com")


# 3. Verify that categories are visible on left side bar
    try:
        assert driver.find_element(By.CSS_SELECTOR, ".left-sidebar > h2:nth-of-type(1)").text == "CATEGORY"
        print("Category is visible")
    except AssertionError:
        print("Category is not visible")


# 4. Click on 'Women' category
    categories = driver.find_elements(By.XPATH, "//div[@id='accordian']/div/div/h4/a")
    category_button = driver.find_elements(By.XPATH, "//div[@id='accordian']/div/div/h4/a/span")

    for x in range(len(categories)):
        if categories[x].text == "WOMEN":
            category_button[x].click()


# 5. Click on any category link under 'Women' category, for example: Dress
    w_sub_cats = driver.find_elements(By.XPATH, "//div[@id='Women']/div/ul/li/a")
    req_w_cat = ["DRESS"]
    for x in range(len(req_w_cat)):
        if w_sub_cats[x].text == req_w_cat:
            w_sub_cats[x].click()


    time.sleep(5)

# 6. Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS' (pseudo code


#    try:
#        assert driver.find_element(By.XPATH,"//h2[text()='WOMEN - DRESS PRODUCTS']").text == "WOMEN - DRESS PRODUCTS"
#        print("Subcategory is visible")
#    except AssertionError:
#       print("Subcategory is not visible")


# 7. On left side bar, click on any sub-category link of 'Men' category
    categories = driver.find_elements(By.XPATH, "//div[@id='accordian']/div/div/h4/a")
    category_button = driver.find_elements(By.XPATH, "//div[@id='accordian']/div/div/h4/a/span")

    for x in range(len(categories)):
        if categories[x].text == "MEN":
            category_button[x].click()


    m_sub_cats = driver.find_elements(By.XPATH, "//div[@id='Men']/div/ul/li/a")
    req_m_cat = ["TSHIRTS"]
    for x in range(len(req_m_cat)):
        if m_sub_cats[x].text == req_m_cat:
            m_sub_cats[x].click()