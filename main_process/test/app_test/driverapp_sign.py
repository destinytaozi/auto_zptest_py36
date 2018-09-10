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
    mTread_sign_01 = myThread_sign_01()
    # mTread_sign_02 = myThread_sign_02()
    # mTread_sign_05 = myThread_sign_05()
    mTread_sign_01.start()
    # mTread_sign_02.start()
    # mTread_sign_05.start()


if __name__ == '__main__':
    main()
    time.sleep(3)

