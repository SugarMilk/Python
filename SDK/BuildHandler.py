# coding: utf-8 python2.7
# created by mr.huangjian@foxmail.com on 2017/7/2.

from datetime import *
import SDKVersionManager
import os

class BuildHandler:

    def __init__(self, mode="", target="", note="", version=""):
        self.time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.mode = mode
        self.target = target
        self.note = note
        self.version = version

    def startBuild(self):
        self.setNewVersion()
        self.setExtraInfo()

    def confirmMessage(self):
        return "【时间】：{time}\n【模式】：{mode}\n【目的】：{target}\n【备注】：{note}\n【版本号】：{version}"\
            .format(time=self.time, mode=self.mode, target=self.target, note=self.note, version=self.version)

    def extraString(self):
        return "#define extra @\"【时间】：{time}\\n【模式】：{mode}\\n【目的】：{target}\\n【备注】：{note}\\n【版本号】：{version}\""\
            .format(time=self.time, mode=self.mode, target=self.target, note=self.note, version=self.version)

    def setNewVersion(self):
        SDKVersionManager.set_new_version(self.version)

    def setExtraInfo(self):
        if not os.path.exists("extraInfo.h"):
            os.system("touch extraInfo.h")
        context = open("extraInfo.h", 'w')
        context.write(self.extraString())
        context.close()

