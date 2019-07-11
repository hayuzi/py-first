# 基本数据类型
# Python3中有六个标准数据类型
# Number String List(列表) Tuple(元组) Set(集合) Dictionary(字典)
# 不可变数据 Number String Tuple
# 可变数据 List Dictionary Set

# ------------
# Number
# 强调 在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
a, b, c, d = 10, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
# 可以使用 isinstance 判断类型
print(isinstance(a, int))
# type()不会认为子类是一种父类类型。 isinstance()会认为子类是一种父类类型。
# 在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加

# 使用del语句删除一些对象引用。( 可以同时删除多个 )
del a
del b, c

# 数值运算
# 数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数(对于两个整数的运算)。
# 在混合计算时，Python会把整型转换成为浮点数。
print( 2 / 4)
print( 2 // 4)
print( 2.1 / 4)
print( 2.10 // 4)

# ----------
# String
# 字符串截取方式     变量[头下标:尾下标]
# 使用 \ 作为转义特殊字符， 字符串前面添加一个 r 便是原始字符串，此时\不转意
# 与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。

# ----------
# List
# 
