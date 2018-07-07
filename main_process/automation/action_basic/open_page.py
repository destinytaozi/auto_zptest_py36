#coding = utf-8
#This file named open_page.py
#His duty is to open the page of all your gived page which has xptah.
from main_process.automation.action_basic.mouse_actions import MouseActions
class OpenPage():
    def open_menu_page(self,driver,m_xpath_first,m_xpath_second):
        driver.find_element_by_xpath(m_xpath_first)
        ma_mmc=MouseActions()
        ma_mmc.mouse_move_click(driver, m_xpath_second)
        driver.find_element_by_xpath(m_xpath_second)
        print("——————菜单打开！——————")
