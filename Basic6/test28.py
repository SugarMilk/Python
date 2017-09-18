# coding: utf-8 python3
# created by mr.huangjian@foxmail.com on 2017/9/18.

import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class ComboBox(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        comBox = QtWidgets.QComboBox(self)
        comBox.move(30, 30)
        comBox.addItem(u"中国")
        comBox.addItem(u"美国")
        comBox.addItem(u"韩国")
        comBox.addItem(u"日本")
        comBox.activated[str].connect(self.comBoxSelected)

        self.setGeometry(300, 300, 300, 300)

    def comBoxSelected(self, text):
        print(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    comBox = ComboBox()
    comBox.show()
    app.exec_()
