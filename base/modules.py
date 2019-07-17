#!/usr/bin/env python3

# 模块
# 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。
# 模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
import sys
from testpackage import testmodules

print('命令行参数如下：')
for i in sys.argv:
    print(i)
print('\n\nPython 路径为：', sys.path, '\n')
testmodules.if_slef_call()

# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回
print(dir(testmodules))
print(dir())
