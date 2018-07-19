# coding=utf-8
"""
-------------------------------------------------------------------
    File Name:       app_basic
    Description:
    Author:          destiny
    date:            2018/7/7 11:56
--------------------------------------------------------------------
    Change Activity:
                    2018/7/7 11:56
--------------------------------------------------------------------
"""
import time

from main_process.automation_app.app_driver import app_driver
from appium import webdriver

__author__ = 'destiny'

class appBasic():
    def driverapp_session_open(self,parameter):
        app_d=app_driver.appDriver()
        desired_caps=app_d.driver_app_driver(parameter['platformName'],parameter['platformVersion'],parameter['deviceName'])
        driver=webdriver.Remote(parameter['appiumURL'], desired_caps)    #'http://localhost:4723/wd/hub'
        # print(driver)
        return driver,desired_caps