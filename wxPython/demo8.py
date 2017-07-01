# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/22.

import wx
import wx.lib.buttons as buttons


app = wx.App()
window = wx.Frame(None, size=(300, 150))
panel = wx.Panel(window, -1)


button = buttons.GenButton(panel, -1, 'Genric Button', size=(100, 40), style=wx.BU_EXACTFIT)
button.Enable(True)

button.SetFont(wx.Font(12, wx.NORMAL, wx.NORMAL, wx.NORMAL, True)) # 设置字体
button.SetBezelWidth(5)             # 3D斜面效果
button.SetBackgroundColour("Navy")  # 背景颜色
button.SetForegroundColour("White") # 字体颜色（前景颜色）

# image = wx.Image('tag2.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
# buttons.GenBitmapButton(panel, -1, image, pos=(110, 0))

# buttons.GenBitmapToggleButton(panel, -1, image)

window.Show()
app.MainLoop()