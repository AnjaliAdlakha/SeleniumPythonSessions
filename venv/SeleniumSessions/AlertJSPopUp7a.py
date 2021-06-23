from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import alert

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('http://mail.rediff.com/cgi-bin/login.cgi')

driver.find_element(By.NAME, 'proceed').click()
time.sleep(3)


driver.switch_to.alert()
print(alert.text)
alert.accept()#accept it , click on ok
#alert.dismiss() #cancel the pop up


driver.switch_to.default_content()


time.sleep(3)
driver.quit()