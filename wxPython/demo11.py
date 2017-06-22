# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/22.

import wx

class GaugeFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, '', size=(350, 150))
        self.SetBackgroundColour("green")
        panel = wx.Panel(self, -1, size=(100, 100), pos=(20, 20))
        panel.SetBackgroundColour("Pink")
        panelnel2 = wx.Panel(self, -1, size=(20, 20), pos=(10, 10))
        panelnel2.SetBackgroundColour("Blue")
        self.count = 0
        self.gauge = wx.Gauge(panel, -1, 50, (20, 50), (250, 30))
        self.gauge.SetBackgroundColour("White")
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        self.Bind(wx.EVT_IDLE, self.onIdle)

    def onIdle(self, event):
        self.count = self.count + 1
        if self.count == 50:
            self.count = 0
        self.gauge.SetValue(self.count)

app = wx.App()
GaugeFrame().Show()
# window = wx.Frame(None, title = "二维码生成器", size = (400, 500))
# window.Show()
app.MainLoop()
