from selenium import webdriver

driver = webdriver.Chrome()


websites = [
    "https://www.google.com",
    "https://www.bbc.com",
    "https://www.apple.com",
    "https://www.cnn.com"
]

for url in websites[1:]:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])

    driver.get(url)




