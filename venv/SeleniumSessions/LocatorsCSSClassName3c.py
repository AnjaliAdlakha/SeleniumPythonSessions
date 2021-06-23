from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)
driver.get("https://app.hubspot.com/login")

print(driver.title)

#driver.find_element(By.CSS_SELECTOR, '#username').send_keys("anjali30@gmail.com")

# driver.find_element(By.CLASS_NAME, 'login-email').send_keys("anjali30@gmail.com")
# driver.find_element(By.CLASS_NAME, 'login-password').send_keys("test@123")
# driver.find_element(By.CLASS_NAME, 'login-submit').click()

#I cannot use 3 classes together with my class name

# driver.find_element(By.CSS_SELECTOR, 'input.form-control.private-form_control.login-email').send_keys("anjali30@gmail.com")


# driver.find_element(By.XPATH, "//input[@class ='form-control.private-form_control.login-email']").send_keys("anjali30@gmail.com")

#all the links on the page return with a tag, a means anchor tag


driver.find_element(By.LINK_TEXT, 'Sign up').click()

driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign').click()



