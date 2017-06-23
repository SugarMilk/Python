# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/22.

import os
import commands
import subprocess

# 调用终端，执行Shell命令
# print os.system('open /Users/huangjian/Desktop/模板')

# print os.popen('ls', 'r').readlines()

# print commands.getstatusoutput('ls')

# print subprocess.call("ls", shell=False)

print subprocess.call("exit 1", shell=True)

print range(1, 10)

