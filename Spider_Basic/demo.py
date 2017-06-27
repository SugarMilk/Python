# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/27.

import urllib

def test_urlopen():
	f = urllib.urlopen("http://yuedu.163.com/")

	print f.getcode(), '\n'
	print f.read(1000), '\n'
	print f.info(), '\n'
	print type(f.info()), '\n'
	print f.info().items(), '\n'
	print f.info().headers, '\n'
	print f.info().getheader('Content-Type'), '\n'

	print help(f.info())

def test_urlretrieve():
    (f, httpmessages) = urllib.urlretrieve("http://yuedu.163.com/", "index.html")

    print f, '\n'
    print httpmessages, '\n'


test_urlretrieve()

