# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/22.

import wx
import wx.lib.buttons as buttons


app = wx.App()
window = wx.Frame(None, size=(300, 150))
panel = wx.Panel(window, -1)

image = wx.Image('tag2.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()

buttons.GenToggleButton(panel, -1, "Toggle Button")

# b = buttons.GenBitmapTextButton(panel, -1, image, "Bitmapped Text",  size=(200, 100))#位图文本按钮
# b.SetUseFocusIndicator(False)

wx.FlexGridSizer()

window.Show()
app.MainLoop()