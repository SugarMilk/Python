# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/14.

import sys
from PyQt5 import QtWidgets, QtGui

app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()
widget.move(600, 300)
widget.resize(500, 500)
widget.setWindowTitle(u"窗口")
widget.setWindowIcon(QtGui.QIcon("logo.png")) # window
widget.show()

sys.exit(app.exec_())
