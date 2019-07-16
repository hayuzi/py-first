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
print([3*x for x in vec])
