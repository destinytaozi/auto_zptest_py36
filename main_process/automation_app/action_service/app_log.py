# coding=utf-8
"""
-------------------------------------------------------------------
    File Name:       app_login
    Description:
    Author:          destiny
    date:            2018/7/7 11:37
--------------------------------------------------------------------
    Change Activity:
                    2018/7/7 11:37
--------------------------------------------------------------------
"""
import string
import time

from main_process.automation_app.app_driver import app_driver
from main_process.automation_app.action_basic.app_basic import appBasic
from appium import webdriver

__author__ = 'destiny'
class appLog():

    def driverapp_login(self,count,pwd,driver):
        time.sleep(5)
        driver.find_element_by_xpath("//android.widget.EditText[@text='请输入账号']").send_keys(count)
        driver.find_elements_by_xpath("//android.widget.EditText")[1].send_keys(pwd)
        driver.find_element_by_xpath("//android.widget.TextView[@text='登 录']").click()
        print('————司机app完成登录！————')

    def driverapp_logout(self,driver):
        print('————退出司机app！————')
        driver.quit()