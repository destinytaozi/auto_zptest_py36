# coding=utf-8
#This file named web_basic_opera.py
#His duty is to login all system(saas、cloud、wms and so on) with all browsers on web.
import time
from selenium import webdriver
# from selenium.webdriver import ActionChains
from main_process.automation.action_basic import mouse_actions

class LoginWeb():
    def __init__(self):
        pass

    # web登录
    def login_web(self, driver, url, userName, password):
        driver.maximize_window()
        driver.get(url)
        # driver.find_element_by_id("remberme").click()
        driver.find_element_by_id("userName").send_keys(userName)
        driver.find_element_by_id("pwd").send_keys(password)
        driver.find_element_by_id("login_id").click()
        time.sleep(1)
        print("——————登录成功！——————")

    def mouse_move_close_page(self,driver,m_xpath):
        self.mouse_actions = mouse_actions.MouseActions()
        self.mouse_actions.mouse_move_click(driver,m_xpath)
        print("——————页面关闭！——————")
