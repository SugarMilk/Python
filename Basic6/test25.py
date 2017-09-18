# coding: utf-8 python3
# created by mr.huangjian@foxmail.com on 2017/9/18.

import sys
from PyQt5 import QtWidgets, QtGui

class ImageView(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        label = QtWidgets.QLabel(self)
        label.setPixmap(QtGui.QPixmap("logo.png"))

        hBoxLayout = QtWidgets.QHBoxLayout(self)
        hBoxLayout.addWidget(label)

        self.setLayout(hBoxLayout)
        self.setGeometry(300, 300, 300, 300)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    image = ImageView()
    image.show()
    app.exec_()
