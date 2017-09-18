# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/15.

import sys
from PyQt5 import QtWidgets

class GridLayout(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        titleLabel = QtWidgets.QLabel("Title")
        authorLabel = QtWidgets.QLabel("Author")
        reviewLabel = QtWidgets.QLabel("Review")

        titleEdit = QtWidgets.QLineEdit()
        authorEdit = QtWidgets.QLineEdit()
        reviewEdit = QtWidgets.QTextEdit()

        gridLayout = QtWidgets.QGridLayout()
        gridLayout.setSpacing(10)

        gridLayout.addWidget(titleLabel, 1, 0)
        gridLayout.addWidget(titleEdit, 1, 1)

        gridLayout.addWidget(authorLabel, 2, 0)
        gridLayout.addWidget(authorEdit, 2, 1)

        # 向网格布局中增加一个组件，可以提供组件的跨行和跨列参数
        # 在这个例子中，我们让reviewEdit组件跨了5行
        # TODO PyQt各种布局的原理是啥

        gridLayout.addWidget(reviewLabel, 3, 0)
        gridLayout.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(gridLayout)
        self.setGeometry(300, 300, 300, 300)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    layout = GridLayout()
    layout.show()
    app.exec_()

