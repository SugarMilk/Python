# coding: utf-8 python3
# created by mr.huangjian@foxmail.com on 2017/9/15.

x = [1, 2, 3]

y = [4, 5, 6, 7]

z = [8, 9, 1, 2, 3]


xy = zip(x, y) # 矩阵


print(xy)  # <zip object at 0x10259d8c8>
print(*xy) # (1, 4) (2, 5) (3, 6)


"""
Ref:
    Python 并行遍历zip()函数使用方法 http://www.iplaypy.com/jinjie/zip.html
    Python: zip()的使用 http://blog.csdn.net/shomy_liu/article/details/46968651
    Python中zip()函数用法实例教程 http://www.jb51.net/article/53051.htm
    Python的zip函数 http://www.cnblogs.com/frydsh/archive/2012/07/10/2585370.html
    python中map()与zip()操作方法 http://www.jb51.net/article/80156.htm

    伯乐在线/脚本之家

"""

