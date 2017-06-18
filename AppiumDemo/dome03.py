#coding=utf-8
# from unittest import TestCase
# import unittest
#
#
# class studunt(TestCase):
#     def setUp(self):
#         print "开始"
#     def testname(self):
#         print  "你好"
#     def name(self):
#         print "不好"
#     def tearDown(self):
#         print "清空"
#
# if __name__=='__main__':
#     unittest.main()
#
# class mini(TestCase):
#     def setUp(self):
#         print "开始"
#     def testname(self):
#         print  "你好"
#     def name(self):
#         print "不好"
#     def tearDown(self):
#         print "清空"
#
# if __name__=='__main__':
#     unittest.main()
# import random
# score=random.randint(1,100)
# guess=0
# tries=0
# print "这是一个数字从1到99。我给你5次"
# while guess != score and tries<5:
#     guess=input('输入要猜的数字：')
#     if guess<score:
#         print "猜小了"
#     elif guess>score:
#         print "猜大了"
#     elif guess==score:
#         print "猜对了"
#         break
#     tries += 1
# else:
#     print "5次机会用完了"
import webbrowser


class ball:

    def bounce(self):
        if self.direction =="down":
         self.direction = "up"

myball=ball()
myball.direction="down"

print "我的球的方向是",myball.direction
print "现在我要反弹球"
print
myball.bounce()
print "现在的方向是",myball.direction


