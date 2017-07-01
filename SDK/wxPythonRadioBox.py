# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/1.

import wx

class RadioBox(wx.RadioBox):
    def __init__(self, superview, choices, onRadioBox=None):
        wx.RadioBox.__init__(self, superview, choices=choices)
        self.Bind(wx.EVT_RADIOBOX, onRadioBox, self)

    def select(self, n):
        self.SetSelection(n)

    def getselect(self):
        return self.GetSelection()

