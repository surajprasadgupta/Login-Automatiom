#download chrome browse from
#https://chromedriver.storage.googleapis.com/index.html?path=2.38/
# download seleniun using pip3 install selenium
from selenium import webdriver
username= 'sgsdgsdgd'
password= 'ffff'
url = 'https://rltrac.com/login/?id=2'
driver = webdriver.Chrome("/home/suraj/Desktop/geckodriver")  
driver.get(url)
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('login_button').click()
driver.find_element_by_id('sidebar_home').click()
driver.find_element_by_id('name_search').click()
