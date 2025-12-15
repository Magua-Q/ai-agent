"""
    常用的魔法方法
    __init__: 在创建对象的时候，会自动调用
    __str__: 输入语句打印对象的时候，会自动调用，默认打印的是内存地址
    __repr__
    __del__: 当对象从内存中被释放的时候，该函数会被自动调用
    __getitem__
    __setitem__

"""


class Car:
    def __init__(self, make, model):
        self.color = make
        self.nums = model

    def __str__(self):
        return "test"

    def __del__(self):
        print(f"{self}对象呗销毁了")

if __name__ == '__main__':
    c1 = Car('黑色', 6)
    print(c1)
    del c1
    # c1.show()