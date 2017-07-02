# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/1.

import wx

class StaticText(wx.StaticText):
    prviate_text = ""

    def __init__(self, superview, style=0):
        wx.StaticText.__init__(self, superview, -1, style=style)

    def text(self, text):
        self.prviate_text = text
        self.SetLabel(text)

    def gettext(self):
        return self.prviate_text

    def minsize(self, minsize):
        self.SetMinSize(minsize)

    def size(self, size):
        self.SetSize(size)

    def origin(self, origin):
        self.SetPosition(origin)

    def font(self, font):
        self.SetFont(wx.Font(font, wx.ROMAN, wx.NORMAL, wx.NORMAL))

    def textcolor(self, textcolor):
        self.SetForegroundColour(textcolor)

    def backgroundcolor(self, backgroundcolor):
        self.SetBackgroundColour(backgroundcolor)

