# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/1.

import wx

class Button(wx.Button):

    def __init__(self, super_view, onClick=None):
        wx.Button.__init__(self, super_view)
        self.Bind(wx.EVT_BUTTON, onClick, self)

    def origin(self, origin):
        self.SetPosition(origin)

    def size(self, size):
        self.DoSetSize(self.GetPosition()[0], self.GetPosition()[1], size[0], size[1], 0)

    def title(self, title):
        self.SetLabel(title)

    def font(self, font):
        self.SetFont(wx.Font(font, wx.ROMAN, wx.NORMAL, wx.NORMAL))

