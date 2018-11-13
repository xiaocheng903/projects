import unittest
from selenium import webdriver
import time


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def login(self,username,password):
        self.driver = webdriver.Chrome()
        self.driver.get("http://qoajxbrms.diandainfo.com/")
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_class_name("btn-submit").click()


    def test_fail(self):
        self.login('12345678910','123123')
        time.sleep(3)
        error = self.driver.find_element_by_class_name("errorMsg").text
        if error == "":
            print("登录成功")
        else:
            print("用户名或密码错误")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
