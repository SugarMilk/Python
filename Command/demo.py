# coding: utf-8 python2.7
# created by mr.huangjian@foxmail.com on 2017/7/4.

import os

"""
/Users/huangjian/PycharmProjects/Python/Command
statusCode: 0
"""

# No.1
# statusCode = os.system("pwd")
# print 'statusCode:', statusCode


"""
/Users/huangjian/PycharmProjects/Python/Command
"""

# No.2
f = os.popen("pwd")
print f.read()

