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
import gc
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
    def sign_all_pay_cash(self, threadParameter):
        # 初始化app
        # try:
        appB = appBasic()
        driver, desired_caps = appB.driverapp_session_open(threadParameter)
        # 登录app
        appLogin = appLog()
        appLogin.driverapp_login(threadParameter['userName'], threadParameter['password'], driver)
        # 签收收款业务流程
        print('设备：', desired_caps['deviceName'], datetime.datetime.now().__format__("%m-%d %H:%M:%S"), ' 开始签收！')
        time.sleep(5)
        sign_bill = signBill()
        # sign_bill.select_date_tab(driver)
        # tab_list=driver.find_elements_by_xpath("//android.widget.HorizontalScrollView/android.view.View")
        i = 0
        # 待签收列表是否配送单
        while sign_bill.judge_tablist(driver) == 1:
            i = i + 1
            sign_bill.select_date_tab(driver)
            sign_bill.wait4sign_list_click(driver)
            time.sleep(2)
            sign_flag = sign_bill.judge_signbutton(driver)
            if 1 == sign_flag:
                random_math = random.randint(1, 10)
                if random_math == 1:
                    sign_bill.sign_refused_list(driver)
                    sign_bill.sign_refused_detail(driver)
                    sign_bill.sign_refused_reason(driver)
                    sign_bill.sign_refused_confirm(driver)
                    time.sleep(1)
                    sign_bill.click_confirm(driver)
                    print(desired_caps['deviceName'], '配送单：', i, datetime.datetime.now().__format__("%H:%M:%S"), '拒签完成')
                    time.sleep(1)
                else:
                    sign_bill.sign_distribution(driver)
                    time.sleep(1)
                    sign_bill.confirm_distribution(driver)
                    sign_bill.confirm_payment(driver)
                    print(desired_caps['deviceName'], '配送单：', i, datetime.datetime.now().__format__("%H:%M:%S"), '全签完成')
                    time.sleep(1)
            else:
                sign_bill.sign_pay(driver)
                sign_bill.confirm_payment(driver)
                print(desired_caps['deviceName'], '配送单：', i, datetime.datetime.now().__format__("%H:%M:%S"), '全签完成')
                time.sleep(1)

            # print(desired_caps['deviceName'],len(driver.find_elements_by_xpath("//android.widget.HorizontalScrollView/android.view.View")))
        print('设备：', desired_caps['deviceName'], datetime.datetime.now().__format__("%m-%d %H:%M:%S"), ' 完成签收！')
    # except Exception as err:
    #     print("异常:%s" % err)
    #     driver.quit()
    #     print('驱动关闭！')
    # else:
    #     driver.quit()
    #     print('驱动关闭！')
