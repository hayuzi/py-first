# 函数
def funcFirst():
    print('hello world')

# python 函数的参数传递：
# 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
# 可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

# 关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
# 以下实例在函数 printme() 调用时使用参数名


def printinfo(name, age=20):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="test name")
printinfo("test name", 100)
printinfo("test name")
printinfo(name="test name")

# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 格式如下
# def functionname([formal_args,] *var_args_tuple ):
#   "函数_文档字符串"
#   function_suite
#   return [expression]

# 打印任何传入的参数


def printinfomulti(arg1, *vartuple):
    print("输出: ")
    print(arg1)
    print(vartuple)


printinfomulti(1, 2, 3, 4, 5)

# 还有一种就是参数带两个星号 **基本语法如下：
# 加了两个星号 ** 的参数会以字典的形式导入。
# def functionname([formal_args,] **var_args_dict ):
#   "函数_文档字符串"
#   function_suite
#   return [expression]

# 声明函数时，参数中星号 * 可以单独出现，如果单独出现星号 * 后的参数必须用关键字传入。例如:


def f(a, b, *, c):
    return a+b+c


f(1, 2, c=3)
