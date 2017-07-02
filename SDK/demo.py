# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/22.

from wxPythonEnum import *
from wxPythonStaticText import StaticText
from wxPythonBitmapButton import BitmapButton
from wxPythonTextfield import Textfield
from wxPythonRadioBox import RadioBox
from wxPythonButton import Button
import ConfigBoard
import wx

app = wx.App()
window = wx.Frame(None, title="好玩友SDK打包工具", size=(500, 270), style=wx.CLOSE_BOX | wx.MINIMIZE_BOX)
panel = wx.Panel(window, -1)

# 设置按钮

def onSettingButtonAction(event):
    ConfigBoard.openConfigBoard(window, "路径配置")

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

targetRadioList = ["接入游戏自测", "给SDK质检测试", "给游戏质检测试"]

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
oldVersionTf.text("3.0.0.8")

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

# 运行Demo工程

def onRunButtonAction(event):
    print "Run..."

runButton = Button(panel, onClick=onRunButtonAction)
runButton.origin((25, 183))
runButton.size((190, 35))
runButton.font(17)
runButton.title("\n运行Demo工程\n")

# 编译打包Framework

def onBuildButtonAction(event):
    print "Build..."
    wx.MessageBox("Build Success", "Message")
    print modeRadio.getselect()
    print targetRadio.getselect()
    print noteTf.gettext()
    print newVersionTf.gettext()


buildButton = Button(panel, onClick=onBuildButtonAction)
buildButton.origin((240, 183))
buildButton.size((200, 35))
buildButton.font(17)
buildButton.title("\n编译打包Framework\n")



window.Show()
app.MainLoop()
