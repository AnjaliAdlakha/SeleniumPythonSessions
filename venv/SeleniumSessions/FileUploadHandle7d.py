from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import alert

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('http://cgi-lib.berkeley.edu/ex/fup.html')

#if type = file is there then

driver.find_element(By.NAME, 'upfile').send_keys('C:\\Users\\anjal\\Desktop\\MyWork.xml')


driver.find_element(By.XPATH, "//input[@type='submit']").click()