# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/15.

import sys
from PyQt5 import QtWidgets, QtCore

class CheckBox(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        checkBox = QtWidgets.QCheckBox(u"星期六", self)
        checkBox.move(20, 20)
        checkBox.stateChanged.connect(self.valueChanged)

        self.setGeometry(300, 300, 300, 300)

    def valueChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.setWindowTitle(u"你选中了")
        else:
            self.setWindowTitle("")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    checkBox = CheckBox()
    checkBox.show()
    app.exec_()

