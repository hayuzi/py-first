

def if_slef_call():
    # 是否自身调用
    if __name__ == '__main__':
        print('程序自身在运行')
    else:
        print('我来自另一模块')
