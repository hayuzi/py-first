# python3输入和输出
import math
import pickle
import pprint

# 输出格式美化
# Python两种输出值的方式: 表达式语句和 print() 函数
# 第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
# 如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
# 如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。

# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。

# str.format() 的基本使用
print('{} 和 {}'.format('hello', 'world'))
print('{0} 和 {1}'.format('hello', 'world'))
print('{1} 和 {0}'.format('hello', 'world'))
print('{first}网址： {second}'.format(first='呵呵', second='哈哈哈'))
print('站点列表 {0}, {1}, 和 {other}。'.format('hello', 'world', other='哈哈哈哈'))
# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
# 可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用
print('{0:10} ==> {1:10d}'.format('test', 1))
# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值
table = {'one': 1, 'two': 2, 'three': 3}
print('one: {0[one]:d}; two: {0[two]:d}; three: {0[three]:d}'.format(table))
# 也可以通过在 table 变量前使用 '**' 来实现相同的功能
print('one: {one:d}; two: {two:d}; three: {three:d}'.format(**table))


# ----------
# 读取键盘输入
# Python提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘。
# input 可以接收一个Python表达式作为输入，并将运算结果返回。
str = input("请输入：")
print("你输入的内容是: ", str)

# 读和写文件
# open() 将会返回一个 file 对象，基本语法格式如下:
f = open("./foo.txt", "w")
f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
# 关闭打开的文件
f.close()

f = open("./foo.txt", "r")
# 除了正常的 f.read(size) 以及 f.readline() 还有 f.readlines() 外，还可以循环迭代其中的内容
for line in f:
    print(line, end='')
f.close()

# ----------
# pickle 模块
# python的pickle模块实现了基本的数据序列和反序列化。
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
# pickle.dump(obj, file, [,protocol])
#   protocol的值可以是1和2（1和2表示以二进制的形式进行序列化。其中，1是老式的二进制协议；2是新二进制协议

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
output = open('data.pkl', 'wb')
pickle.dump(data1, output)
output.close()

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

pkl_file.close()
