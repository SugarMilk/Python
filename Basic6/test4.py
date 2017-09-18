# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/14.

import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

label = QtWidgets.QLabel("<h1 style='color:red; font-family:Times New Roman'>Setting</h1>") # Qt文本支持HTML
label.show()

statusCode = app.exec_()
sys.exit(statusCode) # 没有这句也行

