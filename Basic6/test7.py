# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/14.

import sys
from PyQt5 import QtWidgets

class InputDialog(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        inputButton = QtWidgets.QPushButton(u"输入对话", self)
        inputButton.move(20, 20) # 绝对定位
        inputButton.clicked.connect(self.showDialog)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.move(130, 20)

        self.setGeometry(800, 300, 300, 300) # 设置位置与尺寸


    def showDialog(self):
        text, result = QtWidgets.QInputDialog.getText(self, u"输入对话", u"输入你的名字") # 输入对话框
        if result:
           self.lineEdit.setText(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    inputDialog = InputDialog()
    inputDialog.show()

    app.exec_()

