from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

def select_values(element, value):
    select = Select(element)
    select.select_by_visible_text(value)


ele_indus = driver.find_element(By.ID, 'Form_submitForm_Industry')
ele_country = driver.find_element(By.ID, 'Form_submitForm_Country')

#now i will call the method and pass the values
select_values(ele_indus, 'Education')
select_values(ele_country, 'India')



#lets say i want to print all the values from the dropdown
#watch video at 13:00
select = Select(ele_indus)
indus_list = select.options

for ele in indus_list:
    print(ele.text)
    if(ele.text == 'Automotive'):
        ele.click()
        break



        


