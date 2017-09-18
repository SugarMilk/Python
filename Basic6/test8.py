# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/14.

import sys
from PyQt5 import QtWidgets, QtGui

class ColorDialog(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        chooseColorButton = QtWidgets.QPushButton(u"选择颜色",  self)
        chooseColorButton.move(20, 20)
        chooseColorButton.clicked.connect(self.showDialog)

        color = QtGui.QColor(0, 0, 0)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setStyleSheet("QWidget {background-color:%s}" % color.name())
        self.frame.setGeometry(130, 22, 100, 100)

        self.setGeometry(800, 300, 300, 300)
        self.setWindowTitle(u"颜色选择对话框")

    def showDialog(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.frame.setStyleSheet("QWidget {background-color:%s}" % color.name())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    colorDialog = ColorDialog()
    colorDialog.show()
    app.exec_()
