from selenium import webdriver
import time
browser = webdriver.Firefox()
time.sleep(5)
browser.get("https://www.instagram.com/")
time.sleep(6)

username=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
password=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
button=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")

username.send_keys("username")
password.send_keys("password")
time.sleep(2)
button.click()






