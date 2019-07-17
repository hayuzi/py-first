# 面向对象

# 不详解
#  类


class ClassName:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    def __init__(self, name, age, w):
        # 构造方法， 在实例化的时候会自动调用, self代表实例, 而不是类
        self.name = name
        self.age = age
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))
