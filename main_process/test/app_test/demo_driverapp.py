# coding = utf-8
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {}
desired_caps['platformName'] = "Android"         # 声明是ios还是Android系统
desired_caps['platformVersion'] = '4.4.2'        # Android内核版本号，可以在夜神模拟器设置中查看
desired_caps['deviceName'] = '127.0.0.1:62001'   # 连接的设备名称
desired_caps['appPackage'] = 'com.zhoupukuaisong'    # apk的包名
desired_caps['appActivity'] = 'com.zhoupukuaisong.MainActivity'  # apk的launcherActivity
desired_caps['appWaitActivity']='com.zhoupukuaisong.MainActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)          # 建立 session
time.sleep(10)
driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'请输入账号')]").send_keys(u'13900000000')
driver.find_elements_by_xpath("//android.widget.EditText")[1].send_keys(u'aA111111')
driver.find_element_by_xpath("//android.widget.TextView[@text='登 录']").click()
print('完成')
# time.sleep(10)
driver.quit()      # 退出 session
