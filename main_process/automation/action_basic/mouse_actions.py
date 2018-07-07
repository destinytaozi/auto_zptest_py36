# coding=utf-8
#This file named mouse_actions.py
#His duty is some operation about mouse event.
import time
from selenium import webdriver
# from selenium.webdriver import ActionChains

class MouseActions():
    def mouse_move_click(self,driver,m_xpath):
        mouseClickjs = '''
                        var evObj = document.createEvent('MouseEvents');
                        evObj.initMouseEvent("click",true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                        arguments[0].dispatchEvent(evObj);
                        '''
        sysSetUserMenuPath = driver.find_element_by_xpath(m_xpath)
        #定位到xpath位置并点击
        driver.execute_script(mouseClickjs,sysSetUserMenuPath)
        time.sleep(5)