# coding: utf-8 python3
# created by mr.huangjian@foxmail.com on 2017/9/18.

import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class LineEdit(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        label = QtWidgets.QLabel(self)
        label.move(60, 40)

        lineEdit = QtWidgets.QLineEdit(self)
        lineEdit.move(60, 100)
        lineEdit.textChanged[str].connect(self.textChanged)

        self.label = label
        self.setGeometry(300, 300, 300, 300)

    def textChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    lineEdit = LineEdit()
    lineEdit.show()
    app.exec_()
