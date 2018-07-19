# coding=utf-8
"""
-------------------------------------------------------------------
    File Name:       driverapp_sign
    Description:
    Author:          destiny
    date:            2018/7/7 12:30
--------------------------------------------------------------------
    Change Activity:
                    2018/7/7 12:30
--------------------------------------------------------------------
"""
from time import strptime

import time
from main_process.automation_app.action_process.sign_all_pay_all import signAllPayAll
from main_process.automation_app.action_process.return_order import returnOrder
from main_process.automation_app.action_process.sign_and_refuse import signAndRefuse
from main_process.thread_process.thread_02 import myThread_sign_02
from main_process.thread_process.thread_01 import myThread_sign_01
__author__ = 'destiny'

def main():
    # threads=[]
    mTread_sign_01=myThread_sign_01()
    mTread_sign_01.start()

    mTread_sign_02=myThread_sign_02()
    mTread_sign_02.start()

    # thread_parameter_1 = {'platformName': 'Android', 'platformVersion': '5.1', 'deviceName': 'MT66-4WA-7K18623', 'appiumURL': 'http://192.168.1.82:4724/wd/hub'}
    # user_info_1 = {'userName': '13711110000', 'password': '111111'}
    # snr = signAndRefuse()
    # snr.sign_all_pay_cash(thread_parameter_1,user_info_1)

    #找一下python打日志文件的方法
    #连接app

    # thread_sign = {'platformName': 'Android', 'platformVersion': '5.1', 'deviceName': 'MT66-4WA-7K18623','appiumURL':'http://localhost:4743/wd/hub'}
    # sign_all=signAllPayAll()
    # sign_all.sign_all_pay_cash(thread_sign['platformName'], thread_sign['platformVersion'], thread_sign['deviceName'],
    #                            thread_sign['appiumURL'])
    # thread_refuse = {'platformName': 'Android', 'platformVersion': '4.4.2', 'deviceName': 'emulator-5554','appiumURL':'http://192.168.1.157:4724/wd/hub'}
    # return_order=returnOrder()
    # return_order.sign_refuse(thread_refuse['platformName'], thread_refuse['platformVersion'], thread_refuse['deviceName'],
    #                          thread_refuse['appiumURL'])
    # _thread.start_new_thread(sign_all.sign_all_pay_cash,(thread_sign['platformName'], thread_sign['platformVersion'], thread_sign['deviceName'],
    #                                                      thread_sign['appiumURL'],))
    # _thread.start_new_thread(return_order.sign_refuse,(thread_refuse['platformName'], thread_refuse['platformVersion'], thread_refuse['deviceName'],
    #                                                    thread_refuse['appiumURL'],))

if __name__ == '__main__':
    main()
    time.sleep(3)

