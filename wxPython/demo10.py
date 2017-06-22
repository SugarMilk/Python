# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/22.

import wx

class SpinnerFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Spinner Example', size=(200, 200))
        panel = wx.Panel(self, -1)
        sc = wx.SpinCtrl(panel, -1, "", (30, 20), (80, -1))
        sc.SetRange(0, 10)
        sc.SetValue(1)


app = wx.App()
spinner = SpinnerFrame()

spinner.Show()

app.MainLoop()

