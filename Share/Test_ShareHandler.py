# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/20.

import ShareHandler
# from ShareHandler import *

print 'ShareHandler.str_app_key:  ', ShareHandler.str_app_key
print 'ShareHandler.str_app_secret:  ', ShareHandler.str_app_secret
print 'ShareHandler.str_redirect_url:  ', ShareHandler.str_redirect_url, '\n'

handler = ShareHandler.ShareHandler()

print '1. handler.app_key:  ', handler.app_key
print '1. handler.app_secret:  ', handler.app_secret
print '1. handler.redirect_url:  ', handler.redirect_url, '\n'

handler.func_set_register_params("wx910b9ad660d63715")

print '2. handler.app_key:  ', handler.app_key
print '2. handler.app_secret:  ', handler.app_secret
print '2. handler.redirect_url:  ', handler.redirect_url, '\n'

print handler.func_get_register_params(), '\n'

tmp_dict = handler.func_get_register_params()

print 'handler.app_key:  ', tmp_dict[ShareHandler.str_app_key]
print 'handler.app_secret:  ', tmp_dict[ShareHandler.str_app_secret]
print 'handler.redirect_url:  ', tmp_dict[ShareHandler.str_redirect_url]

