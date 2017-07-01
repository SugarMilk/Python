# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/21.

import wx

app = wx.App()

window = wx.Frame(None, -1, "Hello", pos = (100, 100), size = (300, 300), style = wx.DEFAULT_FRAME_STYLE, name = "frame")

# window.CreateStatusBar(2, wx.STB_DEFAULT_STYLE)
window.CreateToolBar(wx.TB_FLAT)

window.Show(True)

app.MainLoop()
