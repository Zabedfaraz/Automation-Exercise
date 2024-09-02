import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
# 1. Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
#close browser
    yield driver
    driver.quit()

def test_automation_prac_tc3(driver):
# 2. Navigate to URL
    driver.get('http://automationexercise.com')


# 3. Verify that home page is visible successfully

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(1) > a").text == "Home"
        print("Home page is visible")
    except AssertionError:
        print("Home page is not visible")



# 4. click on the signup/login button
    login_button = driver.find_element(By.XPATH,"/html//header[@id='header']/div[@class='header-middle']//ul[@class='nav navbar-nav']//a[@href='/login']")
    login_button.click()


# 5. Verify 'Login to your account' is visible

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".login-form > h2").text == "Login to your account"
        print("'Login to your account' is visible")
    except AssertionError:
        print("'Login to your account' is not visible")

# 6. Enter incorrect email address and password
    driver.find_element(By.CSS_SELECTOR, ".login-form > form[method='post'] > input[name='email']").send_keys("wrongemail@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "form[method='post'] > input[name='password']").send_keys("wrongpassword")


# 7. Click 'login' button
    driver.find_element(By.CSS_SELECTOR, ".login-form > form[method='post'] > .btn.btn-default").click()


# 8. Verify error 'Your email or password is incorrect!' is visible

    try:
        assert driver.find_element(By.CSS_SELECTOR, ".login-form > form[method='post'] > p").text == "Your email or password is incorrect!"
        print("'Your email or password is incorrect!' is visible")
    except AssertionError:
        print("'Your email or password is incorrect!' is not visible")


