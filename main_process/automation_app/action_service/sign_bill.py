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
        time.sleep(2)
        driver.find_elements_by_xpath("//android.widget.HorizontalScrollView/android.view.View")[0].click()
        # print('————已选调度时间段————')

    #待签收列表页 签收
    def wait4sign_list_click(self,driver):
        time.sleep(2)
        # print(driver.find_elements_by_xpath("//android.widget.TextView[contains(@text,'配送单号: ')]"))
        driver.find_elements_by_xpath("//android.widget.TextView[contains(@text,'配送单号: ')]")[0].click()
        # print('————进入配送详情————')

    #配送单 全签
    def sign_distribution(self,driver):
        time.sleep(2)
        # print(driver.find_element_by_xpath("//android.widget.TextView[@text='签收']"))
        driver.find_element_by_xpath("//android.widget.TextView[@text='签收']").click()
        # print("————签收完成————")

    #直接收款
    def pay_distributio(self,driver):
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.TextView[@text='收款']").click()

    #撤销已签收状态 回到待签收
    def cancel_sign(self,driver):
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.TextView[@text='撤销']").click()

    # 配送详情确认
    def confirm_distribution(self,driver):
        time.sleep(1)
        # print('确认元素：',driver.find_element_by_xpath("//android.widget.TextView[@text='确认']"))
        driver.find_element_by_xpath("//android.widget.TextView[@text='确认']").click()
        # print("————签收确认完成————")

    # 配送单填写应收款并确定
    def confirm_payment(self,driver):
        time.sleep(6)
        getText = driver.find_elements_by_xpath("//android.widget.TextView")[8].text.split('￥')[1]
        getT = round(float(getText),2)
        print("应付款：",getText)
        # print("现金后输入框：",driver.find_element_by_xpath("//android.widget.TextView[@text='现金']/following-sibling::android.widget.EditText[1]"))
        driver.find_element_by_xpath("//android.widget.TextView[@text='现金']/following-sibling::android.widget.EditText[1]").send_keys(getText)
        driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
        # print("————收款完成————")

    # 配送单拒签-列表页
    def sign_refused_list(self, driver):
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.TextView[@text='拒签']").click()

    # 配送单拒签-明细页
    def sign_refused_detail(self,driver):
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.TextView[@text='拒绝签收']").click()

    # 配送单拒签-原因
    def sign_refused_reason(self, driver):
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.TextView[@text='其它']").click()

    # 配送单拒签-原因
    def sign_refused_confirm(self, driver):
        driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()

    #确认
    def click_confirm(self,driver):
        driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()


