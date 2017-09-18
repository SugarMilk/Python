# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/15.

import sys
from PyQt5 import QtWidgets, QtGui

class CheckButton(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        color = QtGui.QColor(0, 0, 0)

        redButton = QtWidgets.QPushButton(u"红色", self)
        redButton.setCheckable(True)
        redButton.move(10, 10)
        redButton.clicked[bool].connect(self.setColor) # TODO 这是什么姿势

        greenButton = QtWidgets.QPushButton(u"绿色", self)
        greenButton.setCheckable(True)
        greenButton.move(10, 60)
        greenButton.clicked[bool].connect(self.setColor)  # TODO 这是什么姿势

        blueButton = QtWidgets.QPushButton(u"蓝色", self)
        blueButton.setCheckable(True)
        blueButton.move(10, 110)
        blueButton.clicked[bool].connect(self.setColor)  # TODO 这是什么姿势

        frame = QtWidgets.QFrame(self)
        frame.setGeometry(150, 20, 100, 100)
        frame.setStyleSheet("QWidget {background-color:%s}" % color.name())

        self.color = color
        self.redButton = redButton
        self.greenButton = greenButton
        self.blueButton = blueButton
        self.frame = frame
        self.setWindowTitle(u"开关按钮")
        self.setGeometry(300, 300, 300, 300)


    def setColor(self, checked):

        if checked:
            value = 255
        else:
            value = 0

        # self.sender() 事件触发源

        if self.sender() == self.redButton:
            self.color.setRed(value)
        elif self.sender() == self.greenButton:
            self.color.setGreen(value)
        else:
            self.color.setBlue(value)

        self.frame.setStyleSheet("QFrame {background-color:%s}" % self.color.name())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    checkButton = CheckButton()
    checkButton.show()
    app.exec_()

