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
    # 选择表头信息：
    def select_date_tab(self, driver):
        time.sleep(2)
        # try:
        driver.find_elements_by_xpath("//android.widget.HorizontalScrollView/android.view.View")[0].click()
        # except Exception as err:
        #     print('表头信息元素没找到，报错%s:',err)
        # # print('————已选调度时间段————')

    def judge_tablist(self, driver):
        time.sleep(2)
        try:
            tab_l = len(driver.find_elements_by_xpath("//android.widget.HorizontalScrollView/android.view.View"))
            if 0 < tab_l:
                return 1
            else:
                return 0
        except Exception as err:
            print("未找到待签收Tab列表，报错:%s" % err)
            return 0

    # 待签收列表页 签收
    def wait4sign_list_click(self, driver):
        time.sleep(2)
        # try:
        # print(driver.find_elements_by_xpath("//android.widget.TextView[contains(@text,'配送单号: ')]"))
        driver.find_elements_by_xpath("//android.widget.TextView[contains(@text,'配送单号: ')]")[0].click()
        # except Exception as err:
        #     print('待签收列表页元素没找到，报错%s:', err)
        # print('————进入配送详情————')

    # 配送单
    def sign_pay(self, driver):
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.TextView[@text='收款']").click()
    # 判断签收按钮是否存在
    def judge_signbutton(self, driver):
        time.sleep(2)
        try:
            sign_x = driver.find_element_by_xpath("//android.widget.TextView[@text='签收']")
            if sign_x:
                return 1
            else:
                return 0
        except Exception as error:
            print('签收按钮没找到，报错:%s' % error)
            print("已签收，直接收款...")
            return 0

    # 配送单 全签
    def sign_distribution(self, driver):
        # print(driver.find_element_by_xpath("//android.widget.TextView[@text='签收']"))
        # try:
        driver.find_element_by_xpath("//android.widget.TextView[@text='签收']").click()
        # except Exception as err:
        #     print('配送明细页签收按钮没找到，报错%s:', err)
        # print("————签收完成————")

    # 直接收款
    def pay_distribution(self, driver):
        time.sleep(1)
        # try:
        driver.find_element_by_xpath("//android.widget.TextView[@text='收款']").click()
        # except Exception as err:
        #     print('配送明细页收款按钮没找到，报错%s:', err)

    # 撤销已签收状态 回到待签收
    def cancel_sign(self, driver):
        time.sleep(1)
        # try:
        driver.find_element_by_xpath("//android.widget.TextView[@text='撤销']").click()
        # except Exception as err:
        #     print('撤销按钮没找到，报错%s:', err)
    # 配送详情确认
    def confirm_distribution(self, driver):
        time.sleep(2)
        # try:
        driver.find_element_by_xpath("//android.widget.TextView[@text='确认']").click()
        # except Exception as err:
        #     print('确认按钮没找到，报错%s:', err)
        # print("————签收确认完成————")

    # 配送单填写应收款并确定
    def confirm_payment(self, driver):
        time.sleep(4)
        # try:
        get_text = driver.find_elements_by_xpath("//android.widget.TextView")[8].text
        # except Exception as err:
        #     print('待签收金额行没找到，报错%s:', err)
        if '零售通' in get_text:
            driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
            time.sleep(1)
            driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
        else:
            text_split = get_text.split('￥')[1]
            # try:
            driver.find_element_by_xpath(
                    "//android.widget.TextView[@text='现金']/following-sibling::android.widget.EditText[1]").send_keys(
                    text_split)
            # except Exception as err:
            #     print('现金输入框没找到，报错%s:', err)
            driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
            time.sleep(1)
            driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
            # print("————收款完成————")

    # 配送单拒签-列表页
    def sign_refused_list(self, driver):
        time.sleep(2)
        # try:
        driver.find_element_by_xpath("//android.widget.TextView[@text='拒签']").click()
        # except Exception as err:
        #     print('拒签按钮没找到，报错%s:', err)
    # 配送单拒签-明细页
    def sign_refused_detail(self, driver):
        time.sleep(2)
        # try:
        driver.find_element_by_xpath("//android.widget.TextView[@text='拒绝签收']").click()
        # except Exception as err:
        #     print('拒签签收按钮没找到，报错%s:', err)
    # 配送单拒签-原因
    def sign_refused_reason(self, driver):
        time.sleep(1)
        # try:
        driver.find_element_by_xpath("//android.widget.TextView[@text='其它']").click()
        # except Exception as err:
        #     print('其他选项没找到，报错%s:', err)
    # 配送单拒签-确定
    def sign_refused_confirm(self, driver):
        # try:
        driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
        # except Exception as err:
        #     print('确定按钮没找到，报错%s:', err)
    # 确认
    def click_confirm(self, driver):
        driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
