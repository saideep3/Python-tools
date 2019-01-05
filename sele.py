import unittest
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.cisco.com")
driver.find_element_by_id("fwt-nav-button").click()
#driver.find_element_by_xpath('//*[@id=\"-tab\"]/div[2]/div[1]/div[1]/div/ul/li[4]/a')
driver.find_element_by_link_text("Switches").click()