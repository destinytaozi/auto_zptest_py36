# coding=utf-8
"""
-------------------------------------------------------------------
    File Name:       sign_and_refuse
    Description:
    Author:          destiny
    date:            2018/7/18 14:04
--------------------------------------------------------------------
    Change Activity:
                    2018/7/18 14:04
--------------------------------------------------------------------
"""
import random

__author__ = 'destiny'


import time
import datetime
from main_process.automation_app.action_service.app_log import appLog
from main_process.automation_app.action_basic.app_basic import appBasic
from main_process.automation_app.action_service.sign_bill import signBill
from main_process.automation_app.action_basic.math_func import mathFunction
__author__ = 'destiny'

class signAndRefuse():
    def sign_all_pay_cash(self,threadParameter,userInfo):
        #初始化app
        appB = appBasic()
        driver,desired_caps = appB.driverapp_session_open(threadParameter)
        # 登录app
        appLogin = appLog()
        appLogin.driverapp_login(userInfo['userName'], userInfo['password'], driver)
        # 签收收款业务流程
        print('设备：', desired_caps['deviceName'], datetime.datetime.now().__format__("%Y-%m-%d %H-%M-%S"),' 开始签收！')
        time.sleep(3)
        sign_bill=signBill()
        # sign_bill.select_date_tab(driver)
        # tab_list=driver.find_elements_by_xpath("//android.widget.HorizontalScrollView/android.view.View")
        i = 0
        math_func=mathFunction()
        while len(driver.find_elements_by_xpath("//android.widget.HorizontalScrollView/android.view.View"))>0:
            i = i+1
            sign_bill.select_date_tab(driver)
            sign_bill.wait4sign_list_click(driver)
            random_math=math_func.random_pick([1,2,3,4],[0.1,0.2,0.3,0.4])
            if random_math == 1:
                sign_bill.sign_refused_list(driver)
                sign_bill.sign_refused_detail(driver)
                sign_bill.sign_refused_reason(driver)
                sign_bill.sign_refused_confirm(driver)
                time.sleep(1)
                sign_bill.click_confirm(driver)
                print(desired_caps['deviceName'],'配送单：', i,'拒签完成')
                time.sleep(2)
            else:
                sign_bill.sign_distribution(driver)
                time.sleep(1)
                sign_bill.confirm_distribution(driver)
                sign_bill.confirm_payment(driver)
                print(desired_caps['deviceName'],'配送单：', i, '全签完成')
                time.sleep(1)
            print(desired_caps['deviceName'],len(driver.find_elements_by_xpath("//android.widget.HorizontalScrollView/android.view.View")))
        print('设备：', desired_caps['deviceName'], datetime.datetime.now().__format__("%Y-%m-%d %H-%M-%S"), ' 完成签收！')
        driver.quit()


