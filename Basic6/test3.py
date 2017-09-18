# coding: utf-8 python3
# created by mr.huangjian@foxmail.com on 2017/9/13.

"""
  简易计算器
"""

from __future__ import division

import sys
from PyQt5 import QtCore, QtWidgets

class Form(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QtWidgets.QTextBrowser()
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setFocus()
        self.lineEdit.selectAll()
        self.lineEdit.setPlaceholderText("Type an expression and press Enter")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)
        # 添加监听
        # self.connect(self.lineEdit, SIGNAL("returnPressed()"), self.updateUi)
        self.lineEdit.textChanged[str].connect(self.textChanged)
        self.setWindowTitle("Calculate")


    def updateUi(self):
        text = ""
        try:
            text = str(self.lineEdit.text()) # unicode("") | u""
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append("<font color=red>%s is invalid!</font>" % text)

    # 监听文本框文本变化

    def textChanged(self, text):
        pass

    # 监听键盘按键事件，重写QDialog方法

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Return:
            self.updateUi()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()


"""
Ref:
    Python中的str与unicode处理方法 http://python.jobbole.com/81244/
    Python 字符编码与解码 http://blog.csdn.net/trochiluses/article/details/16825269
    Python 字符编码总结 http://blog.csdn.net/Setul/article/details/52203894
    Python 编码小结 http://www.wklken.me/posts/2013/08/31/python-extra-coding-intro.html

    Python模块之信号 http://www.cnblogs.com/madsnotes/articles/5688681.html
    四、Python Signal 信号 http://blog.csdn.net/alvine008/article/details/24454159

    PyQt5学习笔记01-第一个窗口 http://blog.csdn.net/a359680405/article/details/45096185
    PyQt5初次体验 http://blog.csdn.net/pdcxs007/article/details/45095293/
    PyQt5教程（七）对话框 http://www.jianshu.com/p/aaa644b5196d

    PyQt4文本框按回车触发事件 http://blog.csdn.net/a6225301/article/details/43316371
    PyQT5 QLineEdit焦点事件触发 https://www.oschina.net/question/331109_2138274

    PyQt5教程(四)——事件与信号 http://blog.csdn.net/baidu_34045013/article/details/52132804
    PyQt5系列教程(四)信号和槽 http://www.cnblogs.com/tkinter/p/5632266.html
    PyQt4获取键盘事件 http://blog.csdn.net/a6225301/article/details/43272303
    如何使用好PyQt4的signal和slot http://blog.csdn.net/lainegates/article/details/8395580
    PyQt4之玩转signal(信号)与slot(槽)一：介绍及简单实例 http://blog.csdn.net/u011943221/article/details/47006549
    PyQt4自定义信号的应用 http://blog.csdn.net/fengqingting2/article/details/50511906

    Python的热更新 http://blog.sina.com.cn/s/blog_6ca0f5eb0102wj6m.html

"""
