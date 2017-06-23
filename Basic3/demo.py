# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/6/23.


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    print 'call wrapper():'
    return wrapper

@log
def now():
    print '2015-3-25'


now()

print [x * 10 for x in range(1, 10) if x % 2 == 0]

print "你好"

