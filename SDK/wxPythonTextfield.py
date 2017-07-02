# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/1.

import wx

class Textfield(wx.TextCtrl):

    def __init__(self, superview, style=0):
        wx.TextCtrl.__init__(self, superview, -1, style=style)

    def text(self, text):
        self.SetLabelText(text)

    def gettext(self):
        return self.GetValue()

    def origin(self, origin):
        self.SetPosition(origin)

    def size(self, size):
        self.SetSize(size)

    def font(self, font):
        self.SetFont(wx.Font(font, wx.ROMAN, wx.NORMAL, wx.NORMAL))

    def textcolor(self, textcolor):
        self.SetForegroundColour(textcolor)

