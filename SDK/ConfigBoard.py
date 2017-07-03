# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/1.

from wxPythonEnum import *
from wxPythonStaticText import StaticText
from wxPythonButton import Button
from wxPythonTextfield import Textfield
from wxPythonFinderDialog import *
import PersistenceUtil
import wx

key_projectFilePath = "projectFilePath"
key_versionFilePath = "versionFilePath"
key_extraFilePath = "extraFilePath"
key_exportDirPath = "exportDirPath"

filePath = "config.json"

def openConfigBoard(superview, title):
    dialog = wx.Dialog(parent=superview, title=title, size=(940, 360))
    dialog.SetPosition((superview.GetPosition()[0], superview.GetPosition()[1]+20))
    panel = wx.Panel(dialog)

    # Framework项目路径

    projectPathLabel = StaticText(panel)
    projectPathLabel.font(16)
    projectPathLabel.text("Framework项目路径")
    projectPathLabel.origin((20, 20))

    def onProjectPathButtonAction(event):
        chooseFile(panel, onselected=onProjectPathSelected)

    projectPathButton = Button(panel, onClick=onProjectPathButtonAction)
    projectPathButton.origin((830, 20))
    projectPathButton.title("选择")

    projectPathTf = Textfield(panel, style=textfieldtype.readonly)
    projectPathTf.origin((20, 45))
    projectPathTf.size((895, 25))
    projectPathTf.textcolor("gray")
    projectPathTf.text(PersistenceUtil.getValueFromJson(filePath, key_projectFilePath))

    def onProjectPathSelected(path):
        projectPathTf.text(path)

    # SDK版本号文件路径

    versionPathLabel = StaticText(panel)
    versionPathLabel.font(16)
    versionPathLabel.text("SDK版本号文件路径")
    versionPathLabel.origin((20, 80))

    def onVersionPathButtonAction(event):
        chooseFile(panel, onselected=onVersionPathSelected)

    versionPathButton = Button(panel, onClick=onVersionPathButtonAction)
    versionPathButton.origin((830, 80))
    versionPathButton.title("选择")

    versionPathTf = Textfield(panel, style=textfieldtype.readonly)
    versionPathTf.origin((20, 105))
    versionPathTf.size((895, 25))
    versionPathTf.textcolor("gray")
    versionPathTf.text(PersistenceUtil.getValueFromJson(filePath, key_versionFilePath))

    def onVersionPathSelected(path):
        versionPathTf.text(path)

    # 额外信息文件路径

    extraPathLabel = StaticText(panel)
    extraPathLabel.font(16)
    extraPathLabel.text("额外信息文件路径")
    extraPathLabel.origin((20, 140))

    def onExtraPathButtonAction(event):
        chooseFile(panel, onselected=onExtraPathSelected)

    extraPathButton = Button(panel, onClick=onExtraPathButtonAction)
    extraPathButton.origin((830, 140))
    extraPathButton.title("选择")

    extraPathTf = Textfield(panel, style=textfieldtype.readonly)
    extraPathTf.origin((20, 165))
    extraPathTf.size((895, 25))
    extraPathTf.textcolor("gray")
    extraPathTf.text(PersistenceUtil.getValueFromJson(filePath, key_extraFilePath))

    def onExtraPathSelected(path):
        extraPathTf.text(path)

    # Framework导出目录

    exportPathLabel = StaticText(panel)
    exportPathLabel.font(16)
    exportPathLabel.text("Framework导出目录")
    exportPathLabel.origin((20, 200))

    def onExportPathButtonAction(event):
        chooseDir(panel, onselected=onExportPathSelected)

    exportPathButton = Button(panel, onClick=onExportPathButtonAction)
    exportPathButton.origin((830, 200))
    exportPathButton.title("选择")

    exportPathTf = Textfield(panel, style=textfieldtype.readonly)
    exportPathTf.origin((20, 225))
    exportPathTf.size((895, 25))
    exportPathTf.textcolor("gray")
    exportPathTf.text(PersistenceUtil.getValueFromJson(filePath, key_exportDirPath))

    def onExportPathSelected(path):
        exportPathTf.text(path)

    # 保存配置

    def onSaveButtonAction(event):
        PersistenceUtil.modifyJson(filePath, key_projectFilePath, projectPathTf.gettext())
        PersistenceUtil.modifyJson(filePath, key_versionFilePath, versionPathTf.gettext())
        PersistenceUtil.modifyJson(filePath, key_extraFilePath, extraPathTf.gettext())
        PersistenceUtil.modifyJson(filePath, key_exportDirPath, exportPathTf.gettext())
        dialog.Close()

    saveButton = Button(panel, onClick=onSaveButtonAction)
    saveButton.origin((200, 270))
    saveButton.size((200, 30))
    saveButton.font(15)
    saveButton.title("\n保存配置\n")

    # 取消关闭

    def onCancelButtonAction(event):
        dialog.Close()

    cancelButton = Button(panel, onClick=onCancelButtonAction)
    cancelButton.origin((500, 270))
    cancelButton.size((200, 30))
    cancelButton.font(15)
    cancelButton.title("\n取消关闭\n")

    dialog.ShowModal()