# coding: utf-8 python2.7
# created by mr.huangjian@foxmail.com on 2017/7/11.

import threading
import time

# http://python.jobbole.com/85050/

def target():
    print 'the curent threading  %s is running' % threading.current_thread().name
    time.sleep(2)
    print 'the curent threading  %s is ended' % threading.current_thread().name
print 'the curent threading  %s is running' % threading.current_thread().name
t = threading.Thread(target=target)
t.setDaemon(True)
t.start()
t.join(1)
print 'the curent threading  %s is ended' % threading.current_thread().name



