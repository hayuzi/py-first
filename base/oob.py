# 面向对象

# 不详解
#  类


class People:
    # 定义基本属性
    name = ''
    age = 0
    # 两个下划线开头，声明该属性为私有，私有属性在类外部无法直接进行访问
    __weight = 0

    def __init__(self, name, age, w):
        # 构造方法， 在实例化的时候会自动调用, self代表实例, 而不是类
        self.name = name
        self.age = age
        self.__weight = w

    def __del__(self):
        # 析构函数，释放对象时使用
        pass

    def __private_methods(self):
        # 私有方法 两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用
        pass

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))

p = People('test', 10, 20)
p.speak()

# class DerivedClassName(BaseClassName1): 这种方法 Man类继承了People
# class DerivedClassName(Base1, Base2, Base3): 还可以多继承
# super() 函数是用于调用父类(超类)的一个方法。
#  super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法
# 方法可以重载


class Man(People):
    def __init__(self, name, age, w):
        # 继承类，并在重载的构造方法中调用被继承类的构造方法。（这个例子只是展示，这里没有必要重载）
        People.__init__(self, name, age, w)

# 类的专有方法：
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方

# 另外，需要注意类属性，实例属性，类方法，实例方法，静态方法的区别
# 这些内容请另行查阅相关资料

# 实例方法
#   定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）；
#   调用：只能由实例对象调用

# 类方法
#   定义：使用装饰器@classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）；
#   调用：实例对象和类对象都可以调用。

# 静态方法
#   定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；
#   调用：实例对象和类对象都可以调用。

# 属性方法（@property）
# @property :属性方法,属性方法的作用就是通过@property把一个方法变成一个静态属性
#   如果想改变属性方法的值，需要使用 @{funcname}.setter 装饰器来定义 setter
#       有了setter以后，使用d.{funcname} = xx的时候就调用了setter方法
#   可以额外设置getter，替换调用property方法来获取属性数据，需要使用 @{funcname}.getter 装饰器来定义 getter
#       写了getter以后，使用x = d.{funcname}的时候就是调用getter方法，而不是直接调用property方法
# 如果想删除这个属性, 需要使用 @{funcname}.deleter 装饰器来定义 deleter
#       写了deleter以后，在调用del 的时候会调用这个方法（ 不设置该方法的 属性方法不可 del ）

# 类的其他各种魔术方法请自行查阅资料
