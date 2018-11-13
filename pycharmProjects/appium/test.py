# # coding=utf-8
# # -*- coding: utf-8 -*-
#
# # from appium import webdriver
#
# import time
#
# desired_caps = {
#
#                 'platformName': 'Android',
#
#                 'deviceName': '30d4e606',
#
#                 'platformVersion': '5.0',
#
#                 'appPackage': 'com.taobao.taobao',
#
#                 'appActivity': 'com.taobao.tao.welcome.Welcome',
#
#                 }
#
# # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#
# # 休眠五秒等待页面加载完成
#
# time.sleep(5)
#
# driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").send_keys("连衣裙").click()
