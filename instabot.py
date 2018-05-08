from selenium import webdriver
import time
from clickie import *
driver = webdriver.Firefox()
driver.get("http://www.instagram.com")
mousemove(20,500)
driver.set_window_size(1000, 1000)
time.sleep(11)
mousemove(45,500)
time.sleep(5)
for i in range(0,10000):
    driver.execute_script("window.scrollTo(0," + str(i*40) + ")")
    time.sleep(0.05)
    mouseclick(45,500)
    time.sleep(0.05)
