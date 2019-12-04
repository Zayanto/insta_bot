from selenium import *
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import request
import time


user_name="zayantokp"
password="9953049100x"


driver=webdriver.Chrome()
z=driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
print(z)

user=driver.find_element_by_name('username')
pass_word=driver.find_element_by_name('password')

user.send_keys(user_name)
pass_word.send_keys(password)

login = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/button')
login.click()
time.sleep(5)

driver.get('https://www.instagram.com/therock/')
#now=driver.find_element_by_link_text('Not Now')
#now.click()

#now2=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[3]/button[2]')
#now2.click()

#search=driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[2]')
#search.send_keys('zayan_singh012')
#zz=driver.get('https://www.instagram.com/zayan_singh012/')


followButton = driver.find_element_by_css_selector('button')
followButton.click()
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
driver.get('http://stackoverflow.com/')
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
driver.get('http://facebook.com/')




