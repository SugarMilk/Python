# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/6/28.

import urllib2

def func():
    url = "http://blog.kamidox.com/no-exist"

    try:
        ins = urllib2.urlopen(url, timeout=3)
    except urllib2.HTTPError, e:
        print e
    else:
        print ins.read(1000)
        ins.close()


func()
