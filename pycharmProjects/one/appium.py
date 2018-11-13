# coding=utf-8

from appium import webdriver

desired_caps = {

                'platformName': 'Android',

                'deviceName': '30d4e606',

                'platformVersion': '5.0',

                # apk包名

                'appPackage': 'com.ddinfo.ddmall.qoa',

                # apk的launcherActivity

                'appActivity': 'com.ddinfo.ddmall.activity.menu.HelloActivity'

                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)