from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\anjal\\Documents\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)

driver.get("http://www.google.com")

driver.find_element(By.NAME, 'q').send_keys("naveen automationlabs")
optionsList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')

print(len(optionsList))

for ele in optionsList:
    print(ele.text)
#gv me the text of each and every element in the list
    if ele.text == 'naveen automationlabs youtube':
        ele.click()
        break


print(driver.title)
time.sleep(5)

#once entire list is available i want to click on naveen automation labs youtube




driver.quit()
