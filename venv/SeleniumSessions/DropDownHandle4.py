from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

ele_indus = driver.find_element(By.ID, 'Form_submitForm_Industry')
select = Select(ele_indus)

select.select_by_visible_text('Education')

#select 4th value from th edropdowns
# select.select_by_index(4)

#in dropdown the value is health but in dropdown it is healthcare
# select.select_by_value('health')


#is multiple method will tell u wether its multi select dropdown or single select dropdown
# print(select.is_multiple)#it will gv none in console

#u can try using select.deselect method also, opp of select

ele_country = driver.find_element(By.ID, 'Form_submitForm_Country')
select_con = Select(ele_country)
select_con.select_by_visible_text('India')

# for 1 or 2 dropdowns it is fine but a generic method is needed



