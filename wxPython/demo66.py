# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/1.

import wx

class Button(wx.Button):

    def __init__(self, super_view):
        wx.Button.__init__(self, super_view)
        self.Bind(wx.EVT_BUTTON, self.func_on_clicked, self)
        self.origin = [0, 0]
        self.size = [0, 0]
        self.title = ''

    def func_set_origin(self, origin):
        self.origin = origin
        self.DoSetSize(self.origin[0], self.origin[1], self.size[0], self.size[1], 0)

    def func_get_origin(self):
        return self.origin

    def func_set_size(self, size):
        self.size = size
        self.DoSetSize(self.origin[0], self.origin[1], self.size[0], self.size[1], 0)

    def func_get_size(self):
        return self.size

    def func_set_title(self, title):
        self.title = title
        self.SetLabel(title)

    def func_get_title(self):
        return self.title

    def func_on_clicked(self, event):
        print 'button clicked...'


app = wx.App()

window = wx.Frame(None, title = "二维码生成器", size = (400, 500))

panel = wx.Panel(window, -1, size=(200, 200))

button = Button(panel)
button.SetFont(wx.Font(20, wx.ROMAN, wx.NORMAL, wx.NORMAL))

button.SetLabel('\n登录\n')

button.func_set_size([100, 50])

window.Show(True)
app.MainLoop()
