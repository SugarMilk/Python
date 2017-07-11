# coding: utf-8 python2.7
# created by mr.huangjian@foxmail.com on 2017/7/12.

from threading import *

def eat():
    for x in range(3):
        print "x:%s" % x

def drink():
    for y in range(3):
        print "y:%s" % y

eat=Thread(target=eat)
eat.start()

drink=Thread(target=drink)
drink.start()

print("主线程结束")
