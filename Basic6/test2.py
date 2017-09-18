# coding: utf-8 python3
# created by mr.huangjian@foxmail.com on 2017/9/13.

"""
 Python Qt Gui 快速编程
 简易小闹钟
 示例： python test2.py 14:30 '起床了！'
"""

import sys, time
from PyQt5 import QtCore, QtWidgets

# sys.argv 表示通过命令行执行当前文件时传递过来的参数，是一个列表

app = QtWidgets.QApplication(sys.argv)

try:
    due = QtCore.QTime.currentTime()
    message = "Wake UP!"

    # raise将异常抛出，被外层的except捕获
    if len(sys.argv) < 2:
        raise ValueError
    hours, mins = sys.argv[1].split(":")
    due = QtCore.QTime(int(hours), int(mins))

    if not due.isValid():
        raise ValueError
    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])

    while QtCore.QTime.currentTime() < due:
        time.sleep(1)  # 睡眠1秒继续轮询

except ValueError:
    message = "Usage: alert.pyw HH:MM [optional message]" # 24hr clock


# 创建标签控件

label = QtWidgets.QLabel("<font color=red size=100><b>" + message + "</b></font>")
label.setWindowFlags(QtCore.Qt.SplashScreen)
label.show()

QtCore.QTimer.singleShot(6000, app.quit) # 单次定时器执行6000ms后退出程序
app.exec_() # 执行程序，事件循环

