# coding=utf-8
import unittest
from appium import webdriver
from time import sleep
#########################################搜微博
#sleep可以搞定程序不稳定性
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

    def test_dl(self):
        # self.Login('15097475275','9581083065')
        self.send('sssssss')

    # def test_send(self):
    #     self.send("lkjsdfljlsjdfjkl")





    def Login(self,usre,passwd):
        sleep(30)
        el = self.driver.find_element_by_name("登录")
        el.click()
        username = self.driver.find_element_by_id('etLoginUsername')

        username.send_keys(usre)
        pwd = self.driver.find_element_by_id('etPwd')
        pwd.send_keys(passwd)
        button = self.driver.find_element_by_name('登录')
        button.click()
        sleep(15)
        yz = self.driver.find_element_by_name('春风冷8').text
        self.assertEqual(u"春风冷8", yz, "cuowu")

        # fx=self.driver.find_element_by_name('发现')
        # fx.click()
        # sosuo=self.driver.find_element_by_id('ly_left')
        # sosuo.click()
        # sosu=self.driver.find_element_by_id('tv_search_keyword')
        #
        # sosu.send_keys('shangren')
        # cd=self.driver.find_element_by_id('iv_search_icon')
        # cd.click()
        # ss=self.driver.find_element_by_name('搜全部')
        # ss.click()



    def element_is_present(self,by,locator):
                        #这是两个形参，你懂的
        try:#尝试
            if by == "id":#如果形参是id的话就返回位真
                self.driver.find_element_by_id(locator)
                return True
            elif by=='name':
                self.driver.find_element_by_name(locator)
                return True
            elif by =='content':
                self.driver.find_element_by_accessibility_id(locator)
                return True
        except:#不是以上属性的就返回为假
            return False




    def login_tc(self):
                                        #这是两个实参和形参相对应的，如果前边输入‘id’后边‘idde参数’他就为你序找id；如果输入的是name就寻找name
        my_button=self.element_is_present("content","我的资料")#寻找我的资料


        while my_button is False:#如果当前页面不存在退出入口就进入循环
            self.driver.press_keycode(4)#找不到就点击返回键（4是手机物理键）
            my_button=self.element_is_present("content","我的资料")#寻找content desc de txst
            #找不到就一直循环

        self.driver.find_element_by_name('我的资料').click()#找到后点击
        self.driver.find_element_by_name('设置').click()
        self.driver.find_element_by_name('帐号管理').click()
        self.driver.find_element_by_name('退出当前帐号').click()
        self.driver.find_element_by_name('确定').click()


    def send(self,wenbo):
        sleep(20)
        self.driver.find_element_by_id('plus_icon').click()
        self.driver.find_element_by_id('composer_item_image').click()
        self.driver.find_element_by_name('分享新鲜事...').send_keys(wenbo)
        self.driver.find_element_by_id('titleSave').click()
        el = self.driver.find_elements_by_xpath(xpath="//android.widget.TextView")

        self.assertIn(u"sssssss",el[4].text)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    assert isinstance(suite, object)
    unittest.TextTestRunner(verbosity=2).run(suite)
