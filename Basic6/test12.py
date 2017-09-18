# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/14.

import sys
from PyQt5 import QtWidgets, QtGui

class Widget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # 全局设置提示（鼠标移入并悬停，显示该提示）
        QtWidgets.QToolTip.setFont(QtGui.QFont("SansSerif", 20))

        button = QtWidgets.QPushButton(u"按钮", self)
        button.setToolTip("<b>button</b>")
        button.move(100, 80)
        button.resize(button.sizeHint())
        button.clicked.connect(QtWidgets.QApplication.quit)  # QtWidgets.QApplication.instance().quit 退出程序

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle(u"QToolTip")
        self.setToolTip("<b>widget</b>")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget()
    widget.show()
    app.exec_()

