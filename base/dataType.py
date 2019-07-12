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
### type()不会认为子类是一种父类类型。 isinstance()会认为子类是一种父类类型。
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
# 列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。 
# 变量[头下标:尾下标]
# 加号 + 是列表连接运算符，星号 * 是重复操作
# 与Python字符串不一样的是，列表中的元素是可以改变的：
# Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4:2])
 
# letters[-1::-1] 有三个参数, 表示翻转获取
#   第一个参数 -1 表示最后一个元素
#   第二个参数为空，表示移动到列表末尾
#   第三个参数为步长，-1 表示逆向
reversedLetters = letters[-1::-1]
print(reversedLetters)

# ----------
# Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改(修改元组元素的操作是非法的)。元组写在小括号 () 里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同
# 元组也可以使用+操作符进行拼接。
tupleA = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

# ----------
# Set（集合）
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# 创建格式：
#   parame = {value01,value02,...}
#   或者
#   set(value)

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'} 
print(student)   # 输出集合，重复的元素被自动去掉
 
# 可以使用in进行成员测试
if 'Rose' in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素


# --------
# Dictionary（字典）
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
# 键(key)必须使用不可变类型。在同一个字典中，键(key)必须是唯一的。
dict0 = {}
dict0['one'] = "1 - 测试"
dict0[2]     = "2 - 测试"
tinydict = {'name': '测试','code':1, 'site': 'www.test.com'}
print (dict0['one'])       # 输出键为 'one' 的值
print (dict0[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

# 构造函数 dict() 可以直接从键值对序列中构建字典
dict2 = dict()
dict3 = dict({'three': 3, 'four': 4}) #可以传递一个字典
dict4 = dict(five=5, six=6) # 传递关键字
dict5 = dict([('seven', 7), ('eight', 8)]) #传一个包含一个或多个元祖的列表
dict6 = dict(zip(['eleven', 'twelve'], [11, 12]))  # 传一个zip()函数

## Python数据类型转换
print(int('123', 10))   # 转整数, 第二个参数为进制数，默认十进制。 如果带base的话，第一个值要传递字符串
print(float(1))         # 函数用于将整数和字符串转换成浮点数。
print(complex(1))       # 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。。
print(complex(1, 2))
print(complex('1+2j'))
print(str(dict0))       # str()函数将对象转化为适于人阅读的形式。
print(repr(dict0))      # repr 函数将对象转化为供解释器读取的形式。
print(eval('pow(2,5)')) # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
tupleB = tuple(letters) # tuple 函数可以以将字符串，列表，字典，集合转化为元组。 
print(tuple(tinydict))  # 将字典转换为元组时，只保留键！
# list() 方法用于将元组或字符串转换为列表。
# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
# dict() 函数用于创建一个字典。
# frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
# chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。 支持十进制与十六进制
print(chr(49))
# ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
# hex() 函数用于将10进制整数转换成16进制，以字符串形式表示。
# oct() 函数将一个整数转换成8进制字符串。






