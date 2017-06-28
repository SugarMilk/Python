# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/28.

# http://www.sodu.cc/map_1.html
# http://chuangshi.qq.com/bang/mo/all-week-2017-05.html?p=3

import urllib

def download_novel_data(novel_list):
    for page in novel_list:
        url = "http://www.sodu.cc/map_%d.html" % page
        file_name = 'page_%d.html' % page

        addinfourl = urllib.urlopen(url)

        if (addinfourl.getcode() == 200):
            (file_path, http_message) = urllib.urlretrieve(url, file_name)

        addinfourl.close()


download_novel_data([1, 2, 3])
