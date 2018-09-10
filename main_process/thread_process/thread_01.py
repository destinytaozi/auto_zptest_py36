# coding=utf-8
"""
-------------------------------------------------------------------
    File Name:       thread_refuse
    Description:
    Author:          destiny
    date:            2018/7/17 20:14
--------------------------------------------------------------------
    Change Activity:
                    2018/7/17 20:14
--------------------------------------------------------------------
"""
import threading
from main_process.automation_app.action_process.sign_and_refuse import signAndRefuse
__author__ = 'destiny'


class myThread_sign_01(threading.Thread):
    def __init__(self):
        # print('线程：反配')
        threading.Thread.__init__(self)
        # self.threadID = threadID
        # self.name = name
        # self.counter = counter

    def run(self):
        thread_info = {'deviceName': 'MT66-4WA-7K18541','appiumURL': 'http://192.168.1.82:4723/wd/hub','userName': '13711110001', 'password': '111111'}
        # 'deviceName': 'MT66-4WA-7K18623','appiumURL': 'http://192.168.1.82:4723/wd/hub'
        print("开始线程：", self.name, '设备：', thread_info['deviceName'])
        snr = signAndRefuse()
        snr.sign_all_pay_cash(thread_info)
        print("退出线程：", self.name, '设备：', thread_info['deviceName'])
