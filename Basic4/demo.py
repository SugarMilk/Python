# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/11.

from plistlib import *

plist = readPlist("info.plist")

print 'plist:', plist

plist["DateTime"] = "2017-07-11"
plist["DateTime"] = "2017-07-11"

writePlist(plist, "info.plist")

print 'plist:', plist
