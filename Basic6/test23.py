# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/15.

import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class ProgressBar(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        progressBar = QtWidgets.QProgressBar(self)
        progressBar.setGeometry(30, 30, 240, 20)
        # progressBar.setValue(20)

        button = QtWidgets.QPushButton(u"开始", self)
        button.move(60, 60)
        button.clicked[bool].connect(self.buttonAction)

        timer = QtCore.QBasicTimer()

        self.progress = 0
        self.progressBar = progressBar
        self.button = button
        self.timer = timer
        self.setGeometry(300, 300, 300, 300)


    def timerEvent(self, event): # 每个QObject类和它的子类都有timerEvent()事件处理函数用于处理定时事件
        if self.progress >= 100:
            self.timer.stop()
            self.button.setText(u"完成")
            self.button.setEnabled(False)
            return

        self.progress += 1
        self.progressBar.setValue(self.progress)


    def buttonAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText(u"开始")
        else:
            self.timer.start(50, self) # 定时器时长和接收定时器事件的对象
            self.button.setText(u"停止")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    progressBar = ProgressBar()
    progressBar.show()
    app.exec_()

