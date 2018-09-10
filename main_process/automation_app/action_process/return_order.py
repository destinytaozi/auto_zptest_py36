# coding=utf-8
"""
-------------------------------------------------------------------
    File Name:       return_order
    Description:
    Author:          destiny
    date:            2018/7/15 9:07
--------------------------------------------------------------------
    Change Activity:
                    2018/7/15 9:07
--------------------------------------------------------------------
"""
import datetime
import time

from main_process.automation_app.action_basic.app_basic import appBasic
from main_process.automation_app.action_service.app_log import appLog
from main_process.automation_app.action_service.sign_bill import signBill

__author__ = 'destiny'

class returnOrder():
    #拒签
    def sign_refuse(self,platformName,platformVersion,deviceName,appiumURL):
        #初始化app
        appB = appBasic()
        driver,desired_caps = appB.driverapp_session_open(platformName,platformVersion,deviceName,appiumURL)
        print(driver)
        #登录app
        appLogin = appLog()
        appLogin.driverapp_login('13711110001', 'aA111111', driver)
        # 签收收款业务流程
        print('设备：', desired_caps['deviceName'], datetime.datetime.now(),' 开始签收！')
        time.sleep(10)
        sign_bill=signBill()
        sign_bill.select_date_tab(driver)
        # tab_list=driver.find_elements_by_xpath("//android.widget.HorizontalScrollView/android.view.View")
        i = 0
        print(driver.find_elements_by_xpath("//android.widget.HorizontalScrollView/android.view.View"))
        while len(driver.find_elements_by_xpath("//android.widget.HorizontalScrollView/android.view.View"))>0:
            i = i+1
            sign_bill.wait4sign_list_click(driver)
            # if len(driver.find_elements_by_xpath("//android.widget.TextView[@text='签收']"))>0:
                # 需要加判断 如果 driver.find_element_by_xpath("//android.widget.TextView[@text='签收']") 不存在 找“存款”
            sign_bill.sign_refused_list(driver)
            sign_bill.sign_refused_detail(driver)
            sign_bill.sign_refused_reason(driver)
            sign_bill.sign_refused_confirm(driver)
            sign_bill.click_confirm(driver)
            time.sleep(2)
            # elif len(driver.find_elements_by_xpath("//android.widget.TextView[@text='收款']"))>0:
            #     sign_bill.cancel_sign(driver)
            #     sign_bill.sign_refused_list(driver)
            #     sign_bill.sign_refused_detail(driver)
            #     sign_bill.sign_refused_reason(driver)
            #     sign_bill.sign_refused_confirm(driver)
            #     sign_bill.click_confirm(driver)
            #     time.sleep(2)
            # else:
            #     print('单据异常')
            #     driver.quit()
        print('设备：' , desired_caps['deviceName'], datetime.datetime.now(),' 完成签收！')
        driver.quit()

    #部分签收
    def sign_partial(self,platformName,platformVersion,deviceName,appiumURL):
        #初始化app
        appB = appBasic()
        driver,desired_caps = appB.driverapp_session_open(platformName,platformVersion,deviceName,appiumURL)
        # 登录app
        # appLogin = appLog()
        # appLogin.driverapp_login('13900000000', 'aA111111', driver)
        # 签收收款业务流程
        print('设备：', desired_caps['deviceName'], datetime.datetime.now(),' 开始签收！')
        time.sleep(5)
        sign_bill=signBill()
        sign_bill.select_date_tab(driver)
        # tab_list=driver.find_elements_by_xpath("//android.widget.HorizontalScrollView/android.view.View")
        i = 0
        while len(driver.find_elements_by_xpath("//android.widget.HorizontalScrollView/android.view.View"))>0:
            i = i+1
            sign_bill.wait4sign_list_click(driver)
            #需要加判断 如果 driver.find_element_by_xpath("//android.widget.TextView[@text='签收']") 不存在 找“存款”
            time.sleep(2)
        print('设备：', desired_caps['deviceName'], datetime.datetime.now(),' 完成签收！')