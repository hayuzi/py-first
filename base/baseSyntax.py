#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# 第一个注释
import sys
print("Hello, Python!")  # 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""

# 行与缩进（ python对缩进要求严格 ）
if True:
    print("True")
else:
    print("False")

# 多行语句 使用 \ 来实现
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
    item_two + \
    item_three

# 在[],{},()中的多行语句不需要使用反斜杠
total2 = ['item_one', 'item_two', 'item_three',
          'item_four', 'item_five']

# ----
# 数字类型
# 四种数字类型 整数，布尔 浮点数 复数
# int 只有一中整数类型 int， 表示为长整型
# bool 如True,False
# float 如 1.23、3E-2
# complex 如 1 + 2j、 1.1 + 2.2j

# 字符串
# 单双引号一样
# 三引号('''或""") 可以指定多行字符串
word = '字符串'
sentence = "这是一个句子。"
paragraph = """哈哈哈hahahah
haha哈哈哈哈"""
print(paragraph)

str = 'test.py'
print(str)
print(str[0:-1])       # 输出第一个到倒数第二个的所有字符
print(str[0])          # 输出第一个字符
print(str[2:5])        # 输出第三个开始到第五个的字符
print(str[2:])         # 输出第三个开始到结尾所有的字符
print(str * 2)          # 输出字符串两次
print(str + '你好')     # 字符串连接
print('hello\nworld')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nworld')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# 等待用户输入
input("\n\n按下 enter 键后退出。")

# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
x = 'write'
sys.stdout.write(x + '\n')

# print不换行输出
print(x, end=" ")

# import 与 from...import
# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *
for i in sys.argv:
    print(i)
print('\n 路径', sys.path)
