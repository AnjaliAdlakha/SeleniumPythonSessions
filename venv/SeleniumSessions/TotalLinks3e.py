from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
# driver.get("https://app.freshworks.com/login")
driver.get("https://amazon.in/")

LinksList = driver.find_elements(By.TAG_NAME, 'a')
#give me the collection of all a tags

print(len(LinksList))
#print the length of the list

#all the links on any web page are associated with a tag

# now i want to print teh text of links, including teh blank links also
for ele in LinksList:
    link_text = ele.text
    print(link_text)


# first print the text of the link and give me the href values also
# attribute method will gv u which attribute do u want
print(ele.get_attribute('href'))

# href means the navigation url reference for each and every link will be printed
# u will see on console that tehre are links available which dont have href property


# give me total number of images present on this particular page
# for images tag name will be img
imageList = driver.find_elements(By.TAG_NAME, 'img')
print(len(imageList))

for ele in imageList:
# for all the images i want to print the value of src i dont have href
#src means from where it is coming
      print(ele.get_attribute('src'))

