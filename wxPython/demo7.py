# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/22.

import wx

class BitmapButton(wx.BitmapButton):
    def __init__(self, super_view):
        image = wx.Image('tag2.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        wx.BitmapButton.__init__(self, super_view, -1, image)
        self.Bind(wx.EVT_BUTTON, self.func_on_clicked, self)

    def func_on_clicked(self, event):
        print 'button clicked...'





app = wx.App()
window = wx.Frame(None, size=(300, 150))
panel = wx.Panel(window, -1)

button = BitmapButton(panel)
button.SetPosition((10, 10))

window.Show()
app.MainLoop()
