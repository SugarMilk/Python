# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/6/28.

import urllib2

def cus_request():
    url = "http://yuedu.163.com/"

    headers = {
        "user-agent":"Mozilla/5.0",
        "x-cus-header":"custom value"
    }

    req = urllib2.Request(url, headers=headers)
    print req.headers

    ins = urllib2.urlopen(req)

    ctx = ins.read(1000)
    print ctx

    ins.close()


cus_request()




