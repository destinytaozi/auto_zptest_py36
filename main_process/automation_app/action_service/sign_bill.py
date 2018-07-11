# coding=utf-8
"""
-------------------------------------------------------------------
    File Name:       sign_bill
    Description:
    Author:          destiny
    date:            2018/7/9 11:51
--------------------------------------------------------------------
    Change Activity:
                    2018/7/9 11:51
--------------------------------------------------------------------
"""
import time

__author__ = 'destiny'


class signBill():
    #选择表头信息：
    def select_date_tab(self,driver):
        driver.find_elements_by_xpath("//android.widget.HorizontalScrollView/android.view.View")[0].click()
        # print('————已选调度时间段————')

    #待签收列表页 签收
    def wait4sign_list_click(self,driver):
        time.sleep(2)
        # print(driver.find_elements_by_xpath("//android.widget.TextView[contains(@text,'配送单号: ')]"))
        driver.find_elements_by_xpath("//android.widget.TextView[contains(@text,'配送单号: ')]")[0].click()
        # print('————进入配送详情————')

    #配送详情页签收
    def sign_distribution(self,driver):
        time.sleep(2)
        # print(driver.find_element_by_xpath("//android.widget.TextView[@text='签收']"))
        driver.find_element_by_xpath("//android.widget.TextView[@text='签收']").click()
        # print("————签收完成————")

    # 配送详情确认
    def confirm_distribution(self,driver):
        time.sleep(2)
        # print('确认元素：',driver.find_element_by_xpath("//android.widget.TextView[@text='确认']"))
        driver.find_element_by_xpath("//android.widget.TextView[@text='确认']").click()
        # print("————签收确认完成————")

    def confirm_payment(self,driver):
        time.sleep(6)
        getText = driver.find_elements_by_xpath("//android.widget.TextView")[8].text.split('￥')[1]
        print("应付款：",getText)
        # print("现金后输入框：",driver.find_element_by_xpath("//android.widget.TextView[@text='现金']/following-sibling::android.widget.EditText[1]"))
        driver.find_element_by_xpath("//android.widget.TextView[@text='现金']/following-sibling::android.widget.EditText[1]").send_keys(getText)
        driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
        driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
        # print("————收款完成————")

    def click_confirm(self,driver):
        driver.find_element_by_xpath("//android.widget.TextView[@text='确定']")


