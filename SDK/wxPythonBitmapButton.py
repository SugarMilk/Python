# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/1.

import wx

class BitmapButton(wx.BitmapButton):
    def __init__(self, superview, imagepath, onclick):
        image = wx.Image(imagepath, wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        wx.BitmapButton.__init__(self, superview, -1, image)
        self.Bind(wx.EVT_BUTTON, onclick, self)

    def origin(self, origin):
        self.SetPosition(origin)



