# login using wrong credentials
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
service_obj = Service("C:/Users/Hp/Downloads/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=option)

driver.implicitly_wait(5)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
mySentence = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
# userName = mySentence[19:48]
userName = mySentence.split(' ')[4]
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.ID, "username").send_keys(userName)
driver.find_element(By.ID, "password").send_keys("password")
driver.find_element(By.CSS_SELECTOR, "label.customradio:nth-child(1) > span:nth-child(3)").click()
dropDown = Select(driver.find_element(By.XPATH, "//select[@class='form-control']"))
dropDown.select_by_visible_text("Teacher")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()
time.sleep(2)
errorMsg = driver.find_element(By.XPATH, "//div[@class='alert alert-danger col-md-12']").text
print(errorMsg)


driver.close()