# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/22.

from wxPythonEnum import aligntype
from wxPythonStaticText import StaticText
from wxPythonBitmapButton import BitmapButton
from wxPythonTextfield import Textfield
from wxPythonRadioBox import RadioBox
import wx

app = wx.App()
window = wx.Frame(None, size=(400, 500), style=wx.CLOSE_BOX | wx.MINIMIZE_BOX)
panel = wx.Panel(window, -1)


radioList = ["a", "b", "c"]

def onRadioBox(event):
    obj = event.GetEventObject()
    print obj.getselect(), '- value: ', radioList[obj.getselect()]

rb = RadioBox(panel, radioList, onRadioBox)
print rb.getselect()


"""
tf = Textfield(panel)
tf.origin((50, 50))
tf.size((200, 50))
tf.font(20)
tf.textcolor("gray")


def onclick(event):
    print event.GetEventObject(), 'button clicked...'

button = BitmapButton(panel, imagepath='.././github.png', onclick=onclick)
button.SetPosition((10, 10))


label = StaticText(panel, aligntype.right)
label.font(20)
label.minsize((150, 50))
label.text("你好Hello")
label.origin((150, 120))
label.backgroundcolor("yellow")
"""

window.Show()
app.MainLoop()
