# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/15.

import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class Slider(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        label = QtWidgets.QLabel(self)
        label.setPixmap(QtGui.QPixmap("voice_n.png"))
        label.setGeometry(20, 20, 40, 40)

        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        # slider.move(20, 20)
        # slider.resize(200, 20)
        slider.setGeometry(60, 30, 200, 20)
        slider.setFocusPolicy(QtCore.Qt.NoFocus)
        slider.valueChanged[int].connect(self.valueChanged)

        self.label = label
        self.setGeometry(300, 300, 300, 300)


    def valueChanged(self, value):
        if value == 0:
            self.label.setPixmap(QtGui.QPixmap("voice_n.png"))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QtGui.QPixmap("voice_s.png"))
        elif value > 30 and value <= 80:
            self.label.setPixmap(QtGui.QPixmap("voice_m.png"))
        else:
            self.label.setPixmap(QtGui.QPixmap("voice_l.png"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    slider = Slider()
    slider.show()
    app.exec_()

