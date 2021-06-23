from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://reddit.com/')
print(driver.get_cookies())

# inspect--> network--> refresh--> network tab--> u will see there are cookies available on
# reddit.com
# driver.getcookies method is available which will return some dictionary
# scroll on a method to know the description.
# dictionary is like hashmap it will store the data in teh form of key and value pair format


driver.add_cookie({"name":"anjalipython","domain":"reddit.com","value":"python"})


cookies = driver.get_cookies()
for cook in cookies:
   print(cook)

