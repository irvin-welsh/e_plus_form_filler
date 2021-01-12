from time import sleep
from selenium import webdriver

browser=webdriver.Firefox()

browser.get('https://e-plus.by/login-eplus-e19/')
sleep(4.1)

username_input=browser.find_element_by_id("username")
password_input=browser.find_element_by_id("auth_password")
login_button=browser.find_element_by_xpath("//*[@id=\"login\"]/div[3]/input")

username_input.send_keys("YOUR_LOGIN")
password_input.send_keys("YOUR_PASSWORD")
login_button.click()
sleep(1.2)

browser.get('https://e-plus.by/#/mvc/publications/admin/addpublication/rubric_id/4/')
sleep(15)


# browser.close()
