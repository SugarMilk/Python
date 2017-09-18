# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/15.

import sys
from PyQt5 import QtWidgets

class GridLayout(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        gridLayout = QtWidgets.QGridLayout()

        texts = ['Clean', 'Back', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)] # 五行四列

        # 矩阵，详见test17.py,
        # TODO 循环遍历，迭代生成元素
        for position, text in zip(positions, texts):
            if text == "":
                continue
            button = QtWidgets.QPushButton(text)
            gridLayout.addWidget(button, * position)

        self.setLayout(gridLayout)
        self.setWindowTitle(u"计算器")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    layout = GridLayout()
    layout.show()
    app.exec_()

