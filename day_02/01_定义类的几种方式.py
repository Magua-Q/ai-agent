"""
通过三种方式定义学生类

object 称基类

其他叫做派生类
"""


# 方式一
# class Student:
#     pass

# 方式二
# class Student():
#     pass
# 方式三
class Student(object):
    pass



if __name__ == '__main__':
    student = Student()
    print(student)