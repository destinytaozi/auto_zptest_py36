# coding = utf-8
#This file named browser_driver.py
#His duty is to driver browsers.
from selenium import webdriver

class BrowserDriver():
   def chrome_driver(self):
       chrome_driver=webdriver.Chrome()
       return chrome_driver

   def firefox_driver(self):
       self.firefox_driver=webdriver.Firefox()
       return self.firefox_driver

   def ie_driver(self):
       self.ie_driver = webdriver.Ie()
       return self.ie_driver