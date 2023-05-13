# Locators : NAME, ID, CSSSelector, Xpath, Classname, linkText

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_service = Service("C:/Users/Hp/Downloads/geckodriver-v0.33.0-win64/geckodriver.exe")
driver = webdriver.Firefox(service=obj_service)
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "name").send_keys("Avinash")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")

'''
Generate CSSSelector :
tagname[attribute='value']
OR - '#id'
OR - .classname
'''
driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("avinash@gmail.com")
driver.find_element(By.CSS_SELECTOR,'#exampleCheck1').click()
# driver.find_element(By.CSS_SELECTOR,'(.form-check-input)[2]').click()
'''
Generate Xpath:
//tagname[@attribute='value'] --> //input[@type='submit']
'''
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert").text
print(message)
assert "Success" not in message

driver.close()