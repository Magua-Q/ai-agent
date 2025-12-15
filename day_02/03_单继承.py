"""
单继承解释
 指的是1一个子类，只能继承自一个父类，子类会从父类中继承属性和行为
"""

class Master:
    def __init__(self):
        self.kongfu = '绝活'

    def make_cake(self):
        print('摊煎饼')

class Prentice(Master):
    pass


if __name__ == '__main__':
    p = Prentice()
    print(p.kongfu)
    p.make_cake()