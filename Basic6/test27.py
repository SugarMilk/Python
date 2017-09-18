# coding: utf-8 python3
# created by mr.huangjian@foxmail.com on 2017/9/18.

import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Splitter(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        topLeft = QtWidgets.QFrame(self)
        topLeft.setFrameShape(QtWidgets.QFrame.StyledPanel)

        topRight = QtWidgets.QFrame(self)
        topRight.setFrameShape(QtWidgets.QFrame.StyledPanel)

        bottom = QtWidgets.QFrame(self)
        bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)

        splitter1 = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topLeft)
        splitter1.addWidget(topRight)

        splitter2 = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hBoxLayout = QtWidgets.QHBoxLayout(self)
        hBoxLayout.addWidget(splitter2)

        self.setLayout(hBoxLayout)
        self.setGeometry(300, 300, 300, 200)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    splitter = Splitter()
    splitter.show()
    app.exec_()
