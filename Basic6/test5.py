# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/14.

import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()

label = QtWidgets.QLabel(widget) # 将label绑定到widget上
label.setText("Hello")

widget.show()

app.exec_()
