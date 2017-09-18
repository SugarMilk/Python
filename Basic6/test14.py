# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/15.

import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        frame = self.frameGeometry() # 获得主窗口的一个矩形特定几何图形。这包含了窗口的框架QRect
        center = QtWidgets.QDesktopWidget().availableGeometry().center() # 算出相对于显示器的绝对值。并且从这个绝对值中，我们获得了屏幕中心点QPoint

        frame.moveCenter(center)
        self.move(frame.topLeft())
        self.resize(300, 300)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()

