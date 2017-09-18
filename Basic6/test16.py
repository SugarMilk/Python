# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/15.

import sys
from PyQt5 import QtWidgets

class BoxLayout(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        OKButton = QtWidgets.QPushButton(u"确定")
        cancelButton = QtWidgets.QPushButton(u"取消")

        hBoxLayout = QtWidgets.QHBoxLayout()
        hBoxLayout.addStretch(1) # 拉伸因子在两个按钮之前增加了一个可伸缩空间(拉伸因子应该是个相对比例)
        hBoxLayout.addWidget(OKButton)
        hBoxLayout.addWidget(cancelButton)

        vBoxLayout = QtWidgets.QVBoxLayout()
        vBoxLayout.addStretch(1) # 拉伸因子将把包含两个按钮的水平箱布局推到窗口的底边
        vBoxLayout.addLayout(hBoxLayout)

        self.setLayout(vBoxLayout)
        self.setGeometry(300, 300, 300, 300)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    box = BoxLayout()
    box.show()
    app.exec_()

