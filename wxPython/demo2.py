# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/21.

import wx

app = wx.App()

window = wx.Frame(None, title = "二维码生成器", size = (400, 500))

panel = wx.Panel(window)
label = wx.StaticText(panel, label = "网址: ", pos = (100,100))

window.Show(True)


app.MainLoop()

