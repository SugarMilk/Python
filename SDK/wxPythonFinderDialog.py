# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/1.

import wx

class FinderDialog:

    def chooseDir(self, superview, title, onselected=None):
        dialog = wx.DirDialog(superview, message=title)
        if dialog.ShowModal() == wx.ID_OK:
            if onselected:
                onselected(dialog.GetPath())
        dialog.Destroy()

    def chooseFile(self, superview, title, onselected=None):
        dialog = wx.FileDialog(superview, message=title)
        if dialog.ShowModal() == wx.ID_OK:
            if onselected:
                onselected(dialog.GetPath())
        dialog.Destroy()
