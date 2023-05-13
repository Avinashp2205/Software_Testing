import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# Invoke Browser
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
service_obj = Service("C:/Users/Hp/Downloads/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=option)
driver.implicitly_wait(15)
action = ActionChains(driver)

driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.XPATH, "//li/a[text()='Shop']").click()
# driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
# driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

productlist = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for items in productlist:
    productname = items.find_element(By.XPATH, "div/h4/a").text
    if productname == "Blackberry":
        items.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//div/ul/li/a").click()
driver.find_element(By.XPATH, "//tr[3]/td[5]/button").click()
driver.find_element(By.CSS_SELECTOR, "#country").send_keys("Ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
# time.sleep(5)
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
successText = driver.find_element(By.CSS_SELECTOR, ".alert-dismissible").text


assert "Success" in successText


time.sleep(5)
driver.close()