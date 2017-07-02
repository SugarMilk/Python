# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/2.

#使用pickle模块将数据对象保存到文件

import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'w')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()

pkl_file = open('data.pkl', 'r')

print pickle.load(pkl_file)

data2 = pickle.load(pkl_file)
print(data2)

# data2 = pickle.load(pkl_file)
# print(data2)