

# explicitly wait is available in the form of webdriver wait class available in python

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://app.hubspot.com/login')
wait = WebDriverWait(driver, 10)
email_id = wait.until(ec.presence_of_element_located(By.ID, 'username'))
email_id.send_keys('test@gmail.com')
driver.get('https://app.hubspot.com/login')