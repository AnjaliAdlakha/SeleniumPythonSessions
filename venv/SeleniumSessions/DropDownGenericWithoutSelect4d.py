from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")



def select_values_from_dropdown(dropDownOptionsList, value):
    print(len(dropDownOptionsList))
    for ele in dropDownOptionsList:
       print(ele.text)
       if ele.text == value:
          ele.click()
          break

indus_options = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_Industry"]/option')
select_values_from_dropdown(indus_options, 'Education')
select_values_from_dropdown(indus_options, 'Travel')

country_options = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_Country"]/option')
select_values_from_dropdown(country_options, 'India')



# indus_options = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_Industry"]/option')
# print(len(indus_options))
# for ele in indus_options:
#     print(ele.text)
#     if ele.text == 'Travel':
#         ele.click()
#         break

#create generic for options method
#so total 3 ways to handle dropdowns


