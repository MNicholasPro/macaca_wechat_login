# -*- coding: utf-8 -*-
'''
@author: April_Chou
@time: 2018/5/22 14:22
'''

import unittest
import time
from macaca import WebDriver
from retrying import retry

desired_caps = {
    'platformName': 'android',
    'package':'com.tencent.mm',
    'activity':'.ui.LauncherUI'
    }

server_url = {
    'hostname': 'localhost',
    'port': 3456
}


class MacacaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.initDriver()

    @classmethod
    @retry
    def initDriver(cls):
        print("Retry connecting server...")
        cls.driver.init()

    def test_01_login(self):

        # 确认弹窗
        self.driver.accept_alert()

        # 确认弹窗
        self.driver.accept_alert()

        # 登录
        self.driver.wait_for_elements_by_id('com.tencent.mm:id/d75')[0].click()

        # 微信号/QQ号/邮箱登录
        self.driver.wait_for_elements_by_id('com.tencent.mm:id/c1t')[0].click()

        # 输入账号
        self.driver.wait_for_elements_by_class_name('android.widget.EditText')[0].send_keys('*****')

        # 输入密码
        self.driver.wait_for_elements_by_class_name('android.widget.EditText')[1].send_keys('*****')

        # 登录
        self.driver.wait_for_elements_by_id('com.tencent.mm:id/c1u')[0].click()

        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()