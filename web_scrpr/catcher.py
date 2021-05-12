from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/")
time.sleep(10)
driver.quit()