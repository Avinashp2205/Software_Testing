# Excercise 2 :

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
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
expectedList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualList = []
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
for item in results:
    print(item.find_element(By.XPATH, 'h4').text)
    actualList.append(item.find_element(By.XPATH, 'h4').text)
print(actualList)
assert expectedList == actualList

driver.close()