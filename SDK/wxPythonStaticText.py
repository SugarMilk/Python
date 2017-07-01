# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/1.

import wx

class StaticText(wx.StaticText):
    def __init__(self, superview, style=0):
        wx.StaticText.__init__(self, superview, -1, style=wx.BORDER_THEME)

    def text(self, text):
        self.SetLabel(text)

    def minsize(self, minsize):
        self.SetMinSize(minsize)

    def size(self, size):
        self.SetSize(size)

    def origin(self, origin):
        self.SetPosition(origin)

    def font(self, font):
        self.SetFont(wx.Font(font, wx.ROMAN, wx.ITALIC, wx.NORMAL))

    def textcolor(self, textcolor):
        self.SetForegroundColour(textcolor)

    def backgroundcolor(self, backgroundcolor):
        self.SetBackgroundColour(backgroundcolor)

