# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/6/30.


import wx

class StaticTextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Static Text Example',
                size=(400, 300))
        panel = wx.Panel(self, -1)

        # 这是一个基本的静态文本
        wx.StaticText(panel, -1, "This is an example of static text", (100, 10))

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = StaticTextFrame()
    frame.Show()
    app.MainLoop()
