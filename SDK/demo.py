# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/22.

from wxPythonEnum import *
from wxPythonStaticText import StaticText
from wxPythonBitmapButton import BitmapButton
from wxPythonTextfield import Textfield
from wxPythonRadioBox import RadioBox
from wxPythonButton import Button
import PathBoard
import wx
import SDKVersionManager
import os
from BuildHandler import BuildHandler

app = wx.App()
window = wx.Frame(None, title="好玩友SDK导出工具", size=(500, 270), style=wx.CLOSE_BOX | wx.MINIMIZE_BOX)
panel = wx.Panel(window, -1)

# 设置按钮

def onSettingButtonAction(event):
    PathBoard.openConfigBoard(window, "路径配置")

settingButton = BitmapButton(panel, imagepath='setting.png', onclick=onSettingButtonAction)
settingButton.origin((450, 10))

# 模式

modeLabel = StaticText(panel)
modeLabel.font(16)
modeLabel.text("模式： ")
modeLabel.origin((20, 20))

# 模式单选

modeRadioList = ["Debug", "Release"]

modeRadio = RadioBox(panel, modeRadioList)
modeRadio.SetPosition((70, 15))

# 目的

targetLabel = StaticText(panel)
targetLabel.font(16)
targetLabel.text("目的： ")
targetLabel.origin((20, 60))

# 目的单选

targetRadioList = [u"接入游戏自测", u"给SDK质检测试", u"给游戏质检测试"]

targetRadio = RadioBox(panel, targetRadioList)
targetRadio.SetPosition((70, 55))

# 备注

noteLabel = StaticText(panel)
noteLabel.font(16)
noteLabel.text("备注： ")
noteLabel.origin((20, 102))

# 备注输入框

noteTf = Textfield(panel)
noteTf.origin((73, 100))
noteTf.size((370, 25))
noteTf.font(15)

# 旧版本号

oldVersionLabel = StaticText(panel)
oldVersionLabel.font(16)
oldVersionLabel.text("旧版本号： ")
oldVersionLabel.origin((20, 143))

# 旧版本号输入框

oldVersionTf = Textfield(panel, style=textfieldtype.readonly)
oldVersionTf.origin((100, 140))
oldVersionTf.size((120, 25))
oldVersionTf.font(16)
oldVersionTf.textcolor("gray")
oldVersionTf.text(SDKVersionManager.get_old_version())

# 新版本号

newVersionLabel = StaticText(panel)
newVersionLabel.font(16)
newVersionLabel.text("新版本号： ")
newVersionLabel.origin((240, 143))

# 新版本号输入框

newVersionTf = Textfield(panel)
newVersionTf.origin((323, 140))
newVersionTf.size((120, 25))
newVersionTf.font(16)

oldVersion = SDKVersionManager.get_old_version()
temp = oldVersion.split('.')
temp[len(temp) - 1] = str(int(temp[len(temp) - 1]) + 1)
newVersion = ".".join(temp)

newVersionTf.text(newVersion)

# 运行Demo工程

def onRunButtonAction(event):
    print "Run..."

runButton = Button(panel, onClick=onRunButtonAction)
runButton.origin((25, 183))
runButton.size((190, 35))
runButton.font(17)
runButton.title("\n运行Demo工程\n")

# 编译导出Framework

def onBuildButtonAction(event):

    mode = modeRadioList[modeRadio.getselect()].encode('utf-8')
    target = targetRadioList[targetRadio.getselect()].encode('utf-8')
    note = noteTf.gettext().encode('utf-8')
    version = newVersionTf.gettext().encode('utf-8')

    buildHandler = BuildHandler(mode, target, note, version)
    confirmDialog = wx.MessageDialog(panel, buildHandler.confirmMessage(), "编译导出前请确认无误",style=wx.YES_NO)

    if confirmDialog.ShowModal() == wx.ID_YES:
        buildHandler.startBuild()


buildButton = Button(panel, onClick=onBuildButtonAction)
buildButton.origin((240, 183))
buildButton.size((200, 35))
buildButton.font(17)
buildButton.title("\n编译导出Framework\n")



window.Show()
app.MainLoop()


