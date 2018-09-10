# coding=utf-8
"""
-------------------------------------------------------------------
    File Name:       thread_demo
    Description:
    Author:          destiny
    date:            2018/7/16 21:18
--------------------------------------------------------------------
    Change Activity:
                    2018/7/16 21:18
--------------------------------------------------------------------
"""
import time
import threading
# from main_process.automation_app.action_process.sign_all_pay_all import signAllPayAll
from main_process.automation_app.action_process.sign_and_refuse import signAndRefuse

__author__ = 'destiny'
exitFlag = 0


class myThread_sign_03(threading.Thread):
    def __init__(self):
        # print('线程：全签')
        threading.Thread.__init__(self)
        # self.threadID = threadID
        # self.name = name
        # self.counter = thread_sign

    def run(self):
        thread_info = {'deviceName': 'MT66-2WA-8F08196','appiumURL': 'http://192.168.100.104:4728/wd/hub','userName': '13711110003', 'password': '111111'}  # 'deviceName': 'MT66-4WA-7K18623','appiumURL': 'http://192.168.1.82:4723/wd/hub'
        print("开始线程：", self.name, '设备：', thread_info['deviceName'])
        sar = signAndRefuse()
        sar.sign_all_pay_cash(thread_info)
        print("退出线程：", self.name, '设备：', thread_info['deviceName'])