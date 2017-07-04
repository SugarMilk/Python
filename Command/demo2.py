# coding: utf-8 python2.7
# created by mr.huangjian@foxmail.com on 2017/7/5.

import os
import commands

"""
(0, '/Users/huangjian/PycharmProjects/Python/Command')
print commands.getstatusoutput("pwd")
"""

"""
(768, 'Hello, Shell! I am Python.')
tuple = commands.getstatusoutput("sh shell.sh")
print tuple[0] >> 8 # 3
"""

print commands.getstatusoutput("sh shell.sh")


