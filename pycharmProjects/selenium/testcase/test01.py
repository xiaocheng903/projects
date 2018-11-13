import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def login(self,username,password):
        self.driver = webdriver.Chrome()
        self.driver.get("http://qoajxbrms.diandainfo.com/")
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_class_name("btn-submit").click()

    def test_success(self):
        self.login('12345678910','123456')
        time.sleep(3)
        print("登录成功")
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/div').click()
        time.sleep(6)
        # self.Select.select_by_value("520001_2200").click()
        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.find_element_by_id('supplierUserCityName').find_element_by_tag_name('option')[3].click()
        # Select(self.driver.find_element_by_id("supplierUserCityName")).select_by_value("520001_2200")

        time.sleep(3)
        self.driver.find_element_by_class_name('btn btn-success').click()
        time.sleep(10)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
