from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('http://classic.crmpro.com/')
time.sleep(4)
username_ele = driver.find_element(By.NAME, 'username')
password_ele = driver.find_element(By.NAME, 'password')
login_button_ele = driver.find_element(By.XPATH,"//input[@type='submit']")


act_chains = ActionChains(driver)
act_chains.send_keys_to_element(username_ele, 'anjaliautomation')
act_chains.send_keys_to_element(password_ele, 'Test@12345')
act_chains.click(login_button_ele).perform()


#problem is it is entering password 2 times instead of single time
#problem was .perform was written multiple times
#check last 5 mins video for hubspot, same code