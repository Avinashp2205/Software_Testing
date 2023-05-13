# Excercise 1 : compare Total amount and discounted amount and make sure that total amount is greater

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
service_obj = Service("C:/Users/Hp/Downloads/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=option)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
items = driver.find_elements(By.XPATH, "//div[@class='products']/div")
for item in items:
    item.find_element(By.XPATH, 'div/button').click()
driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
message = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(message)
totalAmount = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
discountedAmt = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
assert int(totalAmount) > float(discountedAmt)

driver.close()