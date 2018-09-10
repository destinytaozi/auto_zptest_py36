# coding=utf-8
# This file named test01_saleorder_bill.py
# His duty is to test billsaleorder process

import sys
import getopt
import time

from main_process.automation.action_basic.web_basic_opera import LoginWeb
from main_process.automation.driver.browser_driver import BrowserDriver
from main_process.automation.action_basic.open_page import OpenPage

def main():
    #数据初始化
    url_saas = "http://192.168.1.212/saas/main"
    username = "15394695999"
    password = "aA111111"
    saas_page_close_xpath = "//div[contains(@tabindex,'-1') and contains(@class,'fancybox-type-inline')]" \
                            "/div[contains(@class,'fancybox-skin')]/a[contains(@title,'关闭')]"
    saas_saleorder_firstlev_xpath="//div[contains(@class,'layout-panel-west')]" \
                                  "/div[contains(@region,'west') and contains(@class,'west-box')]/div[contains(@id,'mainMenu')]/div[contains(@class,'menu-item')]/div[contains(@class,menu-text)]/span[text()='销售']"
        #"//div[id=]/div[contains(@class,'menu-item')]/div[contains(@class,'menu-text')]/span[text()='销售']"
    saas_saleorder_secondlev_xpath = "//div[contains(@class,'file-und-menu menu')]/div[contains(@level,'3')]/div[@class='menu-text' and text()]"

    # 初始化浏览器驱动
    bdriver = BrowserDriver()
    driver_chrome = bdriver.chrome_driver()
    # 登录系统
    login_web = LoginWeb()
    login_web.login_web(driver_chrome, url_saas, username, password)
    # time.sleep(4)
    #关闭saas公告首页
    login_web.mouse_move_close_page(driver_chrome,saas_page_close_xpath)
    #打开销售订单
    open_saleorder_page=OpenPage()
    open_saleorder_page.open_menu_page(driver_chrome,saas_saleorder_firstlev_xpath,saas_saleorder_secondlev_xpath)

if __name__ == "__main__":
    main()