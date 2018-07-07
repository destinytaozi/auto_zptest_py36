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
    def driverapp_session_open(self):
        app_d=app_driver.appDriver()
        desired_caps=app_d.driver_app_driver()
        driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return driver

