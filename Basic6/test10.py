# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/14.

import sys
from PyQt5 import QtWidgets

class FinderDialog(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        textEdit = QtWidgets.QTextEdit()

        openFileAction = QtWidgets.QAction(u"打开", self)
        openFileAction.setShortcut("Ctrl+O")
        openFileAction.setStatusTip(u"打开新文件")
        openFileAction.triggered.connect(self.showDialog)

        menuBar = self.menuBar()
        fileMenuBar = menuBar.addMenu("&文件")
        fileMenuBar.addAction(openFileAction)

        self.textEdit = textEdit
        self.setCentralWidget(textEdit)
        self.setGeometry(300, 300, 300, 300)
        self.statusBar()


    def showDialog(self):
        # 弹出文件选择框，返回元组
        # 第一个字符串参数，是getOpenFileName()方法的文件路径。
        # 第二个字符串参数，指定了对话框的工作目录。默认文件过滤器设置为All Files (*)

        file = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "/home/")
        filePath = file[0]

        if filePath:
            f = open(filePath, 'r')
            with f:                     # 这是什么姿势？
                data = f.read()
                self.textEdit.setText(data)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    finder = FinderDialog()
    finder.show()
    app.exec_()

