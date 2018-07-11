# coding=utf-8
"""
-------------------------------------------------------------------
    File Name:       sign_all_pay_all
    Description:
    Author:          destiny
    date:            2018/7/9 17:57
--------------------------------------------------------------------
    Change Activity:
                    2018/7/9 17:57
--------------------------------------------------------------------
"""
import time

from main_process.automation_app.action_service.sign_bill import signBill
__author__ = 'destiny'

class signAllPayAll():
    def sign_all_pay_cash(self,driver):
        time.sleep(5)
        sign_bill=signBill()
        sign_bill.select_date_tab(driver)
        # tab_list=driver.find_elements_by_xpath("//android.widget.HorizontalScrollView/android.view.View")
        i=0
        while len(driver.find_elements_by_xpath("//android.widget.HorizontalScrollView/android.view.View"))>0:
            i+=1
            sign_bill.wait4sign_list_click(driver)
            sign_bill.sign_distribution(driver)
            sign_bill.confirm_distribution(driver)
            sign_bill.confirm_payment(driver)
            print("配送单：",i,'完成签收')
        print('单据全部完成签收')

