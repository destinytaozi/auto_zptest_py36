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
        thread_refuse = {'platformName': 'Android', 'platformVersion': '5.1', 'deviceName': 'MT66-2WA-8F08195',
                         'appiumURL': 'http://192.168.100.104:4724/wd/hub'}#127.0.0.1:62001 http://192.168.1.82:4724/wd/hub
        user_info = {'userName': '13711110001', 'password': '111111'}
        print("开始线程：" + self.name)
        snr = signAndRefuse()
        snr.sign_all_pay_cash(thread_refuse,user_info)
        print("退出线程：" + self.name)