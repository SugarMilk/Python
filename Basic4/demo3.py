# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/11.

from plistlib import *

plist = {}

plist["DateTime"] = "2017-07-11"
plist["Configuration"] = "Debug"

writePlist(plist, "info.plist")

print 'plist:', plist
