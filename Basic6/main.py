# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/13.

import sys
import demo

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = demo.Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())

