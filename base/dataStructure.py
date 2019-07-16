# python3的数据结构

# 列表
# 列表可以当作栈来使用 (先进后出处)
# 列表可以当作队列使用（先进先出）


# 也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。
# 列表推导式F
# 列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
# 每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。
# 返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。
vec = [2, 4, 6]
vec1 = [2, 4, -6]
vec2 = [4, 3, -9]
print([3*x for x in vec])
print([[x, x**2] for x in vec])  # 二维
print([3*x for x in vec if x > 3])  # 带条件
print([x*y for x in vec1 for y in vec2])  # 双重循环
print(vec1[i]*vec2[i] for i in range(len(vec1)))
print([str(round(355/113, i)) for i in range(1, 6)])  # 嵌套


# 嵌套列表解析
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])  # 3x4转换为 4x3

# del语句
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]  # 删除 index 2与3，不包含4
print(a)
del a

# 元组
# 元组在输出时总是有括号的，以便于正确表达嵌套结构。
# 在输入时可能有或没有括号， 不过括号通常是必须的（如果元组是更大的表达式的一部分）
t = 12345, 54321, 'hello!'
u = t, (1, 2, 3, 4, 5)

# 集合
a = {x for x in 'abracadabra' if x not in 'abc'}


# 字典
# 此外，字典推导可以用来创建任意键和值的表达式词典
print({x: x**2 for x in (2, 4, 6)})
# 遍历技巧
# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# 反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
for i in reversed(range(1, 10, 2)):
    print(i)

# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
