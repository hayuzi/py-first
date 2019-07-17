# 异常处理

# 语法错误是错误
# 异常是 语法正确，但是执行时候出现错误。

# 异常处理使用 try except 格式
# 与其他一些语言一样，责任链的模式，如果不做 except获取，会反馈到上一层.
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("that was no valid number, try again  ")

# 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如
#   except (RuntimeError, TypeError, NameError):
#        pass

# 最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。
# try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。
# 这个子句将在try子句没有发生任何异常的时候执行。

#   try:
#       ......
#   except OSError:
#       ......
#   except:
#       print("Unexpected error:", sys.exc_info()[0])
#       raise
#   else:
#       ......


# 抛出异常使用 raise
# raise 的异常必须是一个异常的实例或者异常的类（ Exception的子类 ）
# raise NameError('HiThere')

# 用户自定义异常
# 你可以通过创建一个新的异常类来拥有自己的异常。
# 异常类继承自 Exception 类，可以直接继承，或者间接继承，例如:
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

# 定义清理行为
# try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为。
# 如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，而又没有任何的 except 把它截住，
# 那么这个异常会在 finally 子句执行后被抛出

# 预定义的清理行为
# 一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。
# 这面这个例子展示了尝试打开一个文件，然后把内容打印到屏幕上:
for line in open("myfile.txt"):
    print(line, end="")
# 以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。
# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")


# python3 assert 断言
# Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
# assert expression [, arguments]


# end
