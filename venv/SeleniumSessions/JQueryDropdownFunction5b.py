from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


import time

def select_values(options_list, value):
   if not value[0] == 'all':

      for ele in drop_list:
         print(ele.text)
         for k in range(len(value)):
            if ele.text == value[k]:
                ele.click()
                break

   else:
       try:
         for ele in options_list:
           ele.click()
       except Exception as e:
           print(e)


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(2)

driver.find_element(By.ID, 'justAnInputBox').click()

time.sleep(2)

drop_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')

# multi selection
# values_list = ['choice 2', ['choice 3', 'choice 6 2 1']]

# single selection
# values_list = ['choice 7']

# select all
values_list = ['all']

select_values(drop_list, values_list)
# select_values(drop_list, 'choice 3')
# select_values(drop_list, 'choice 6 2 1')


#single selectin, multi selection and select all these values, 3 use cases are there
