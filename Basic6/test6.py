# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/14.

import sys
from PyQt5 import QtWidgets

class LoginDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)

        usernameLabel = QtWidgets.QLabel(u"用户:")
        passwordLabel = QtWidgets.QLabel(u"密码:")
        self.usernameLineEdit = QtWidgets.QLineEdit()
        self.passwordLineEdit = QtWidgets.QLineEdit()
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        gridLayout = QtWidgets.QGridLayout()
        gridLayout.addWidget(usernameLabel, 0, 0, 1, 1)
        gridLayout.addWidget(passwordLabel, 1, 0, 1, 1)
        gridLayout.addWidget(self.usernameLineEdit, 0, 1, 1, 3)
        gridLayout.addWidget(self.passwordLineEdit, 1, 1, 1, 3)

        submitButton = QtWidgets.QPushButton(u"确定")
        cancelButton = QtWidgets.QPushButton(u"取消")
        submitButton.setEnabled(True)
        cancelButton.setEnabled(False)
        submitButton.clicked.connect(self.submitAction) # 添加按钮点击监听事件
        cancelButton.clicked.connect(self.cancelAction)

        hBoxLayout = QtWidgets.QHBoxLayout()
        hBoxLayout.addWidget(submitButton)
        hBoxLayout.addWidget(cancelButton)
        hBoxLayout.setSpacing(60)

        vBoxLayout = QtWidgets.QVBoxLayout()
        vBoxLayout.addLayout(gridLayout)
        vBoxLayout.addLayout(hBoxLayout)
        vBoxLayout.setContentsMargins(40, 40, 40, 40)
        vBoxLayout.addStretch(40)

        self.setLayout(vBoxLayout)
        self.setWindowTitle(u"登录")
        self.resize(300, 200)

    def submitAction(self):
        if self.usernameLineEdit.text().strip() == u"huangjian" and self.passwordLineEdit.text().strip() == u"123456":
            print(u"登录成功")
        else:
            QtWidgets.QMessageBox.warning(self, u"警告", u"用户名或密码错误", QtWidgets.QMessageBox.Yes) # 弹出消息框

    def cancelAction(self):
        print(sys._getframe().f_code.co_name) # 获取当前方法(函数)的名称



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    loginDialog = LoginDialog()
    loginDialog.show()

    app.exec_()
