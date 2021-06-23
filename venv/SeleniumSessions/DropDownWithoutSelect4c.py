from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

# def select_values(element, value):
#     select = Select(element)
#     select.select_by_visible_text(value)
#
#
# ele_indus = driver.find_element(By.ID, 'Form_submitForm_Industry')
# ele_country = driver.find_element(By.ID, 'Form_submitForm_Country')
#
# select_values(ele_indus, 'Education')
# select_values(ele_country, 'India')

indus_options = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_Industry"]/option')
print(len(indus_options))
for ele in indus_options:
    print(ele.text)
    if ele.text == 'Travel':
        ele.click()
        break