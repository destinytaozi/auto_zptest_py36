# coding=utf-8
"""
-------------------------------------------------------------------
    File Name:       app_driver
    Description:
    Author:          destiny
    date:            2018/7/7 11:41
--------------------------------------------------------------------
    Change Activity:
                    2018/7/7 11:41
--------------------------------------------------------------------
"""
__author__ = 'destiny'

class appDriver():
    def driver_app_driver(self,platformName,platformVersion,deviceName):
        desired_caps={}
        desired_caps['platformName'] = platformName   # 声明是ios还是Android系统 例如："Android"
        desired_caps['platformVersion'] = platformVersion  # Android内核版本号，可以在夜神模拟器设置中查看 例如：'4.4.2'
        desired_caps['deviceName'] = deviceName  # 连接的设备名称 例如：'127.0.0.1:62001'
        # desired_caps['app'] = 'E://'#如果要安装app app的路径
        desired_caps['appPackage'] = 'com.zhoupukuaisong'  # apk的包名
        desired_caps['appActivity'] = 'com.zhoupukuaisong.MainActivity'  # apk的launcherActivity
        desired_caps['appWaitActivity'] = 'com.zhoupukuaisong.MainActivity'
        # desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyBoard"] = True
        return desired_caps