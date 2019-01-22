# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class helloWebtest(unittest.TestCase):

    def test_open(self):
        driver = webdriver.Remote(
            command_executor='http://10.4.34.162:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

        PostUrl = "https://y.qq.com/n/yqq/song/001VySE80MYPrC.html"
        driver.get(PostUrl)
        musicname=driver.find_element_by_class_name('data__name_txt').text
        try:
            assert musicname in "喜欢你"
            print("打开成功")
        except Exception as e:
            print("打开失败")
