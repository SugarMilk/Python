# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/20.

str_app_key = "app_key"
str_app_secret = "app_secret"
str_redirect_url = "redirect_url"

class ShareHandler:

    def __init__(self):
        self.app_key = None
        self.app_secret = None
        self.redirect_url = None

    def func_set_register_params(self, app_key, app_secret = None, redirect_url = None):
        self.app_key = app_key
        self.app_secret = app_secret
        self.redirect_url = redirect_url

    def func_get_register_params(self):
        return {
                str_app_key: self.app_key,
                str_app_secret: self.app_secret,
                str_redirect_url: self.redirect_url,
                }

