from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(2)

driver.find_element(By.ID, 'justAnInput_Box').click()

time.sleep(2)

drop_list = driver.find_elements(By.CSS_SELECTOR, 'span.combpTreeItemTitle')


for ele in drop_list:
    print(ele.text)
    if ele.text == 'choice 6 2 3':
        ele.click()
        break




