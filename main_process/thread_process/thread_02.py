# coding=utf-8
"""
-------------------------------------------------------------------
    File Name:       my_thread
    Description:
    Author:          destiny
    date:            2018/7/16 21:07
--------------------------------------------------------------------
    Change Activity:
                    2018/7/16 21:07
--------------------------------------------------------------------
"""
import time
import threading
# from main_process.automation_app.action_process.sign_all_pay_all import signAllPayAll
from main_process.automation_app.action_process.sign_and_refuse import signAndRefuse
__author__ = 'destiny'
exitFlag = 0

class myThread_sign_02(threading.Thread):
    def __init__(self):
        # print('线程：全签')
        threading.Thread.__init__(self)
        # self.threadID = threadID
        # self.name = name
        # self.counter = thread_sign
    def run(self):
        thread_sign = {'platformName': 'Android', 'platformVersion': '5.1', 'deviceName': 'MT66-4WA-7K18541',
                       'appiumURL': 'http://192.168.100.104:4723/wd/hub'}# 'deviceName': 'MT66-4WA-7K18623','appiumURL': 'http://192.168.1.82:4723/wd/hub'
        user_info = {'userName':'13711110000','password':'111111'}
        print ("开始线程：" , self.name,'设备：',thread_sign['deviceName'])
        sar = signAndRefuse()
        sar.sign_all_pay_cash(thread_sign,user_info)
        print ("退出线程：" + self.name,'设备：',thread_sign['deviceName'])