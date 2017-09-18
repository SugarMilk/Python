# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/9/12.


def test1():
    """
    '>>>' 表示要执行的程序，下一行表示输出的预期结果。如果运行结果与预期结果不符会抛出错误，否则没有任何输出。

    >>> 1 == 1
    True
    """

    print(test1.__name__)


def test2():
    """
    '>>>' 表示要执行的程序，下一行表示输出的预期结果。如果运行结果与预期结果不符会抛出错误，否则没有任何输出。

    >>> 1 == 2
    True
    """

    print(test2.__name__)


# 单独执行本.py文件时运行以下代码

if __name__ == "__main__":
    """
    导入doctest模块进行当前文件的单元测试, 执行多行注释里面的测试用例
    """
    import doctest
    doctest.testmod()

