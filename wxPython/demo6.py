# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/21.

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




app = wx.App()

window = wx.Frame(None, title = "二维码生成器", size = (400, 500))

panel = wx.Panel(window, -1, size=(200, 200))

def onClick(event):
    print "5678iop"

button = Button(panel, onClick=onClick)
button.font(20)
button.title('\n登录\n')
button.origin((20, 20))
button.size((200, 50))

window.Show(True)

app.MainLoop()
