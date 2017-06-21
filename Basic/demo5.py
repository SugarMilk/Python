# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/21.

# 同时使用 *args和 *kwargs 时，必须将 *args 参数放置在 ** kwargs 前

# 可变参数 *args (表示任何多个无名参数, 是一个 tuple 元组)

def function(arg1, *args):
    print 'arg1:  ', arg1
    print 'args:  ', args, type(args), '\n'

# function(1, 2, 3, 4)


# 可变参数 **kwargs (表示关键字参数, 是一个 dict 字典)

def function2(*args, **kwargs):
    print 'args:  ', args, '  type:  ', type(args)
    print 'kwargs:  ', kwargs, 'kwargs:  ', type(kwargs), '\n'

# function2(1, 2, 3, 4, 5, 6)
# function2(qq = 1, qzone = 2, wechat = 3)
# function2(1, 2, None, qq = 3, qzone = 4)

# 应用：枚举

# example1

def new_enum(**enum_values):
    return type('Enum', (), enum_values) # 我也不懂这啥意思

type = new_enum(qq = 1, qzone = 2, wechat = 3)

# print type.qq
# print type.qzone

# help(type)

# example2





