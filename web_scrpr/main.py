import time

topic = input("topic to rabbit hole into? ")

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
def catcher(topic):
    driver = webdriver.Firefox()
    wiki = "https://en.wikipedia.org/wiki/" + topic
    driver.get(wiki)
    time.sleep(2)
    # still in testing grounds...
    ##text = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[5]/div[1]/p[2]")
    ##print(text)
    time.sleep(2)
    driver.quit()
    

catcher(topic)


"""
needs to integrate information first to create rabbit hole functionality
perhaps it needs a physical or digital body to go along with the knowledge integration
"""
