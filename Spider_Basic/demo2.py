# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/27.

import urllib
import urlparse

dict = {
    "nickname": "卡路里",
    "uid": "101305"
}

str_dict_encode = urllib.urlencode(dict) # help(urllib.urlencode)
print str_dict_encode # nickname=%E5%8D%A1%E8%B7%AF%E9%87%8C&uid=101305

parse_qs = urlparse.parse_qs(str_dict_encode)
print parse_qs # {'nickname': ['\xe5\x8d\xa1\xe8\xb7\xaf\xe9\x87\x8c'], 'uid': ['101305']}

url = "https://www.baidu.com/s?wd=%E7%88%AC%E8%99%AB&rsv_spt=1&rsv_iqid=0x9c8ed63d000007e1&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=5&rsv_sug1=5&rsv_sug7=100&rsv_sug2=0&inputT=2387&rsv_sug4=2388"

parse_result = urlparse.urlparse(url)
print parse_result
print parse_result.scheme
print parse_result.netloc
print parse_result.query
print urlparse.parse_qs(parse_result.query)



