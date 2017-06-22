# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/21.

import wx

class Button(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Button Example", size = (300, 100))
        panel = wx.Panel(self, -1)
        self.button = wx.Button(panel, -1, "Hello", pos = (50, 20), size=(50, -1))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()

    def OnClick(self, event):
        print 'event:  ', event
        self.button.SetLabel("Clicked")

app = wx.App()
window = Button()
window.Show()
app.MainLoop()
