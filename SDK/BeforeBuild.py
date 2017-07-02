# coding: utf-8 python2.7
# created by mr.huangjian@foxmail.com on 2017/7/2.

from datetime import *

def buildInfomation(mode="", target="", note="", version=""):
    time_ = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    alertString = \
"""\
【时间】：{time}
【模式】：{mode}
【目的】：{target}
【备注】：{note}
【版本号】：{version}\
""".format(time=time_, mode=mode, target=target, note=note, version=version)

    extraString = \
"""\
#define extra @"\\
【时间】：{time}\\n\\
【模式】：{mode}\\n\\
【目的】：{target}\\n\\
【备注】：{note}\\n\\
【版本号】：{version}\\
"
""".format(time=time_, mode=mode, target=target, note=note, version=version)

    return (alertString, extraString)

