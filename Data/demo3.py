# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/2.

import json

a = '{"isOK": 1, "isRunning": "None", "isError": "None"}'

# JSON字符串转字典

dict = json.loads(a)
print dict
print dict["isOK"]
print repr(dict)

# 字典转JSON字符串

print json.dumps({"name":"huangjian"})


