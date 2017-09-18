# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/15.

import sys
from PyQt5 import QtWidgets

class CloseWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("关闭提示框")

    def closeEvent(self, event):
        # 最后一个参数设定默认选中YES/NO按钮
        reply = QtWidgets.QMessageBox.question(self, "Message", "你确定退出吗",
                                               QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CloseWindow()
    window.show()
    app.exec_()
