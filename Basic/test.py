# coding: utf-8

class User:

    def __init__(self, username):
        self.username = username

    def func_get_username(self):
        return self.username

user = User("huangjian")
username = user.func_get_username()

print 'username: ', username
