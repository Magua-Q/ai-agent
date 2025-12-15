"""
继承

继承的好处：
1、 提高代码的复用性
2. 让类和类之间产生关系，是多态的前提

弊端：
    类与类之间的耦合性增强了


开发原则：
    高内聚、低耦合
"""


class Father(object):
    def __init__(self):
        self.gender= "男"

    def walk(self):
        print('father')



class Son(Father):
    pass


if __name__ == '__main__':
    s = Son()
    print(s.gender)
    s.walk()