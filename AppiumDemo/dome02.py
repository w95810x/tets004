#coding=utf-8
import unittest
from appium import webdriver
from time import sleep


class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        proposal={}
        proposal['platformName'] = 'Android'
        proposal['platformVersion'] = '4.4'
        proposal['deviceName'] = '5a20c8c'
        proposal['appPackage']='com.sina.weibo'
        proposal['appActivity'] = 'com.sina.weibo.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',proposal)

    def tearDown(self):

        self.driver.quit()

    def testLogin(self):
        sleep(30)
        el=self.driver.find_element_by_name("登录")
        el.click()
        username = self.driver.find_element_by_id('etLoginUsername')

        username.send_keys("15097475275")
        pwd = self.driver.find_element_by_id('etPwd')
        pwd.send_keys("9581083065")
        button = self.driver.find_element_by_name('登录')
        button.click()
        sleep(15)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


