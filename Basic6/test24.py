# coding: utf-8 python3
# created by mr.huangjian@foxmail.com on 2017/9/18.

import sys
from PyQt5 import QtWidgets, QtCore

class Calendar(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        calendar = QtWidgets.QCalendarWidget(self)
        calendar.move(200, 20)
        calendar.setGridVisible(True)
        calendar.clicked[QtCore.QDate].connect(self.dateChanged)

        label = QtWidgets.QLabel(self)
        label.move(20, 100)
        label.setText(calendar.selectedDate().toString())

        self.label = label
        self.setGeometry(300, 300, 600, 300)


    def dateChanged(self, date):
        self.label.setText(date.toString())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    calendar = Calendar()
    calendar.show()
    app.exec_()

