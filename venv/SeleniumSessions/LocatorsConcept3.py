from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

print(driver.title)

#creating the element and performing the action
#driver.find_element(By.ID, 'Form_submitForm_subdomain').send_keys("anjali automation")
#benefit of below statement is u dont have to write driver.findElement again and again
username_url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
first_name = driver.find_element(By.ID, 'Form_submitForm_FirstName')
last_name = driver.find_element(By.ID, 'Form_submitForm_LastName')
email = driver.find_element(By.ID, 'Form_submitForm_Email')
feature_link = driver.find_element(By.LINK_TEXT, 'Features')


username_url.send_keys("anjali automation")
first_name.send_keys("anjali")
last_name.send_keys("Hans")
email.send_keys("anjali@gmail.com")
feature_link.click()