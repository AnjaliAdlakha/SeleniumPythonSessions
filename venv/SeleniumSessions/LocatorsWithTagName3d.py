from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)
driver.get("https://app.freshworks.com/login")

header_element = driver.find_element(By.TAG_NAME, 'h1')
print(header_element.text)

print(driver.title)


