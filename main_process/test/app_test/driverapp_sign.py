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
import datetime
from main_process.automation_app.action_service.app_log import appLog
from main_process.automation_app.action_basic.app_basic import appBasic
from main_process.automation_app.action_process.sign_all_pay_all import signAllPayAll
import datetime
__author__ = 'destiny'

def main():
    #连接app
    appB = appBasic()
    driver = appB.driverapp_session_open()
    #登录app
    appLogin = appLog()
    appLogin.driverapp_login('13900000000', 'aA111111',driver)
    #签收收款业务流程
    print(datetime.datetime.now())
    sign_all=signAllPayAll()
    sign_all.sign_all_pay_cash(driver)
    print(datetime.datetime.now())

if __name__=='__main__':
    main()




