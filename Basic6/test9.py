# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/14.

import sys
from PyQt5 import QtWidgets

class FontDialog(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        button = QtWidgets.QPushButton(u"选择字体", self)
        button.move(20, 20)
        button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed) # ?
        button.clicked.connect(self.showDialog)

        label = QtWidgets.QLabel(u"好好学习，天天向上！", self)
        label.move(130, 20)

        vBoxLayout = QtWidgets.QVBoxLayout()
        vBoxLayout.addWidget(button)
        vBoxLayout.addWidget(label)

        self.label = label
        self.setLayout(vBoxLayout)
        self.setGeometry(300, 300, 300, 300)

    def showDialog(self):
        font, result = QtWidgets.QFontDialog.getFont()
        if result:
            self.label.setFont(font)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    fontDialog = FontDialog()
    fontDialog.show()
    app.exec_()


"""
Ref:
    QLineEdit、QLabel字体大小、颜色设置 http://blog.csdn.net/u013687602/article/details/19395473
"""
