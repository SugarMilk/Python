# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/15.

import sys
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        exitAction = QtWidgets.QAction(u"&退出", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip(u"退出应用")
        exitAction.triggered.connect(QtWidgets.qApp.quit) # 退出程序

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu(u"文件&(F)")
        fileMenu.addAction(exitAction)

        self.statusBar().showMessage(u"状态栏消息")
        self.setWindowTitle(u"状态栏示例")
        self.setGeometry(300, 300, 400, 300)

        textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(textEdit) # 将textEdit设置成QMainWindow的中心组件，中心组件占据了所有剩下的空间


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
