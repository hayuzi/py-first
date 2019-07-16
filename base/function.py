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
    # "打印任何传入的字符串"
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


# 匿名函数
# python 使用 lambda 来创建匿名函数。
# lambda 只是一个表达式，函数体比 def 简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
# 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
# lambda 函数的语法只包含一个语句，如下：
# lambda [arg1 [,arg2,.....argn]]:expression


def sum(arg1, arg2): return arg1 + arg2


# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))


# return语句
# return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
def sumB(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
total = sumB(10, 20)
print("函数外 : ", total)


# 变量作用域
# Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
# 变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
# L （Local） 局部作用域
# E （Enclosing） 闭包函数外的函数中
# G （Global） 全局作用域
# B （Built-in） 内置作用域（内置函数所在模块的范围）
# 以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内置中找。
g_count = 0  # 全局作用域


def outer():
    o_count = 1  # 闭包函数外的函数中

    def inner():
        i_count = 2  # 局部作用域

# 内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它。
# 在Python3.0中，可以使用以下的代码来查看到底预定义了哪些变量:
# >>> import builtins
# >>> dir(builtins)

# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
# 也就是说这些语句内定义的变量，外部也可以访问.

# 全局变量和局部变量
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
# 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
# 调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。


total = 0  # 这是一个全局变量
# 可写函数说明


def sumC(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sumC(1, 2)
print("函数外是全局变量 : ", total)
# 以上实例输出结果：
#   函数内是局部变量 :  3
#   函数外是全局变量 :  0


# global 和 nonlocal关键字
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
# 以下实例修改全局变量 num：
num = 1


def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)


fun1()
print(num)

# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，如下实例：


def outerfunc():
    num = 10

    def innerfunc():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    innerfunc()
    print(num)


outerfunc()
