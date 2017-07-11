# coding: utf-8 python2.7
# created by mr.huangjian@foxmail.com on 2017/7/11.

import wx


class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(350, 250))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        l3 = wx.StaticText(panel, -1, "多行文本")

        hbox3.Add(l3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t3 = wx.TextCtrl(panel, size=(200, 100), style=wx.TE_MULTILINE | wx.TE_READONLY)

        hbox3.Add(self.t3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox3)
        self.t3.Bind(wx.EVT_TEXT_ENTER, self.OnEnterPressed)

        # http://www.cnblogs.com/dream397/p/3925436.html
        # http://wiki.woodpecker.org.cn/moin/WxPythonInAction/ChapterSeven
        str = "fdsaf\n""12345"

        self.t3.SetValue(str)

        self.t3.SetBackgroundColour("green")

        self.t3.AppendText("vsalkfad")

        self.t3.SetStyle(0, 5, wx.TextAttr("white", "black"))

        panel.SetSizer(vbox)

        self.Centre()
        self.Show()
        self.Fit()

    def OnKeyTyped(self, event):
        print event.GetString()

    def OnEnterPressed(self, event):
        print "Enter pressed"

    def OnMaxLen(self, event):
        print "Maximum length reached"


app = wx.App()
Mywin(None, 'TextCtrl实例-www.yiibai.com')
app.MainLoop()


