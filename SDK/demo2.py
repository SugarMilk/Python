# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/22.

from wxPythonFinderDialog import FinderDialog
import wx


###############################################################################
class DirDialog(wx.Frame):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, -1, u"文件夹选择对话框")
        b = wx.Button(self, -1, u"文件夹选择对话框")
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


    # ----------------------------------------------------------------------
    def OnButton(self, event):
        def ondirpath(path):
            print path

        dialog = FinderDialog()
        dialog.chooseFile(self, "fd", onselected=ondirpath)

        """"""
        # dlg = wx.DirDialog(self, u"选择文件夹", style=wx.DD_DEFAULT_STYLE)

        # dlg = wx.FileDialog(self, u"选择文件")
        # if dlg.ShowModal() == wx.ID_OK:
        #     print dlg.GetPath()  # 文件夹路径
        #
        # dlg.Destroy()


###############################################################################
if __name__ == '__main__':
    frame = wx.PySimpleApp()
    app = DirDialog()
    app.Show()
    frame.MainLoop()
