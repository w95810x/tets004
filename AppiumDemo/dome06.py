# coding=utf-8
import unittest
from appium import webdriver
from time import sleep
def swipe(param, param1, param2, param3, param4):
    pass


class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        proposal = {}
        proposal['platformName'] = 'Android'
        proposal['platformVersion'] = '4.4'
        proposal['deviceName'] = '5a20c8c'
        proposal['appPackage'] = 'com.sina.weibo'
        proposal['appActivity'] = 'com.sina.weibo.SplashActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', proposal)
    def tearDown(self):
        self.driver.quit()

    def testLogin(self):
        sleep(30)
        self.driver.swipe(100,225,100,800,3000)
        sleep(3)
        el = self.driver.find_element_by_name("登录")
        el.click()
        username = self.driver.find_element_by_id('etLoginUsername')

        username.send_keys("15097475275")
        pwd = self.driver.find_element_by_id('etPwd')
        pwd.send_keys("9581083065")
        button = self.driver.find_element_by_name('登录')
        button.click()
        sleep(15)
        dj = self.driver.find_element_by_name('我的资料')
        dj.click()
        cd = self.driver.find_element_by_id('plus_icon')
        cd.click()
        wz = self.driver.find_element_by_id('composer_item_image')
        wz.click()
        nr = self.driver.find_element_by_name('分享新鲜事...')
        nr.send_keys('sssssssssss')
        fs = self.driver.find_element_by_id('titleSave')
        fs.click()
        dz=self.driver.find_element_by_id('cabWeibo')
        dz.click()
        jr=self.driver.find_element_by_id('tv_feed_like_count')
        jr.click()
        wc=self.driver.find_element_by_id('mblogHeadtitle')
        wc.click()







if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    assert isinstance(suite, object)
    unittest.TextTestRunner(verbosity=2).run(suite)
