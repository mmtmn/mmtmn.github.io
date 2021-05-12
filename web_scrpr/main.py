import time

topic = input("topic to rabbit hole into? ")

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
def catcher(topic):
    driver = webdriver.Firefox()
    a = "https://en.wikipedia.org/wiki/" + topic
    driver.get(a)
    time.sleep(10)
    driver.quit()

catcher(topic)
