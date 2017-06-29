# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/6/29.

import urllib
import urllib2

"""
基类与派生类的关系

- BaseHandler
    - ProxyHandler *
    - UnknownHandler *
    - AbstractHTTPHandler
        - HTTPHandler *
        - HTTPSHandler *
    - FTPHandler *
    - FileHandler *
    - HTTPRedirectHandler *
    - HTTPDefaultErrorHandler *
    - HTTPErrorProcessor *
    - HTTPCookieProcessor
"""

def cus_request_debug():

    url = "http://www.douban.com/"

    headers = {
        "user-agent":"Mozilla/5.0"
    }

    data = {
        "username":"calorie",
        "password":"a123456"
    }

    data = urllib.urlencode(data)

    req = urllib2.Request(url=url, headers=headers, data=data)

    """
    创建一个open打开器，如果不传参数，它就传系统默认的Handler，
    如果传递参数给它，如果系统默认有的就替换，否则就添加
    """

    opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))

    ins = opener.open(req)
    print ins.read(1000)

    ins.close()


def install_debug_handler():
    opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1),
                                  urllib2.HTTPSHandler(debuglevel=1))
    """
    将Handler安装到系统默认区，打开时就是这里要安装的opener
    """
    urllib2.install_opener(opener)


install_debug_handler()
cus_request_debug()



