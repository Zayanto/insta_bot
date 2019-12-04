import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome()
z=driver.get('https://www.instagram.com')
print(z)

email_new='bonas.41.50@gmail.com'
full_name_new='bonas'
user_name_new= 'zzz'
password_new='9953049100x'


email=driver.find_element_by_name('emailOrPhone')
full_name=driver.find_element_by_name('fullName')
user_name=driver.find_element_by_name('username')
password=driver.find_element_by_name('password')

email.send_keys(email_new)
full_name.send_keys(full_name_new)
user_name.send_keys(user_name_new)
password.send_keys(password_new)



signup = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[7]/div/button')
signup.click()
time.sleep(10)

def unique_name():
    unique_name=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[5]/div/div[2]/div/button/span')
    x=unique_name.click()
    return x


zzz=unique_name()
print(zzz)


signup = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[7]/div/button')
signup.click()
time.sleep(10)


