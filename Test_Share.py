# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/20.

import Share.ShareHandler
from Share.ShareHandler import ShareHandler

handler = ShareHandler()
handler.func_set_register_params("wx910b9ad660d63715")

tmp_dict = handler.func_get_register_params()

print(tmp_dict[Share.ShareHandler.str_app_key])


