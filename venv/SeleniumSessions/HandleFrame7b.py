#in modern applications hardly u will see frames
#frame is a webelement
#webbrowser--> webpage --> webelements
#webbrowser--> webpage --> frame ---> webelements


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import alert

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('http://londonfreelance.org/courses/frames/index.html')

#below are teh options to switch to frame
#driver.switch_to.frame(2) #pass the index of the frame, index is risky so we shouldnot use it
#driver.switch_to.frame('main')
frame_element = driver.find_element(By.NAME, 'main')
driver.switch_to.frame(frame_element)

headerValue = driver.find_element(By.CSS_SELECTOR, 'body>h2').text
print(headerValue)

driver.switch_to.default_content() #u need to come back
driver.switch_to.parent_frame()
