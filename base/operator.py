# ------------
# 运算符
# Python运算符优先级
#       运算符                          描述
#       **	                        指数 (最高优先级)
#       ~ + -                       按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
#       * / % //                    乘，除，取模和取整除
#       + -                         加法减法
#       >> <<	                    右移，左移运算符
#       &	                        位 'AND'
#       ^ |	                        位运算符
#       <= < > >=                   比较运算符
#       <> == !=                    等于运算符
#       = %= /= //= -= += *= **=	赋值运算符
#       is is not                   身份运算符
#       in not in	                成员运算符
#       and or not	                逻辑运算符

# ------------
# 流程控制
# python中没有 switch case语句，没有 do while 循环
# if elif else 分枝语句
import sys
a = 1
b = 1
if a == 1 and b == 2:
    print('a == 1 and b == 2')
elif a == 1 and b != 2:
    print('a == 1 and b != 2')
elif a != 1 and b == 2:
    print('a != 1 and b == 2')
else:
    print('a != 1 and b !== 2')

# 循环语句
# 我们可以通过设置条件表达式永远不为 false 来实现无限循环
# while 循环还可以使用 else 语句
# 在 while … else 在条件语句为 false 时执行 else 的语句块：
while a < 10:
    print(a)
    a += 1
else:
    print('a >= 10')
# 类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中

# for循环
languages = ["C", "C++", "PHP", "python"]
for x in languages:
    if (x == 'PHP'):
        break
    print(x)
else:
    print('else')

# range() 函数来做循环
for i in range(5):
    print(i, end=",")
print('--')

for i in range(1, 10):
    print(i, end=",")
print('--')

for i in range(1, 10, 3):
    print(i, end=",")
print('--')

for i in range(-10, -110, -20):
    print(i, end=",")
print('--')

# break和continue语句及循环中的else子句
# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
# continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,
# 但循环被break终止时不执行

# pass 语句
# Python pass是空语句，是为了保持程序结构的完整性。pass 不做任何事情，一般用做占位语句.

# ------------
# 迭代器与生成器
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
# 字符串，列表或元组对象都可用于创建迭代器：
listA = [1, 2, 3, 4]
it = iter(listA)
print(next(it))
print(next(it))
# 迭代器对象可以使用常规for语句进行遍历：
for x in it:
    print(x)
# 或者在 while循环中使用 next() 来迭代遍历

# 迭代器创建与完成
# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__()
# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，
# 在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# 生成器
# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值,
# 并在下一次执行 next() 方法时从当前位置继续运行。


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
