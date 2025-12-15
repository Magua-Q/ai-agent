
"""
    self: 谁调用谁，self就是谁

"""

class Car:
    def run(self):
        print(f'汽车会跑: self={self}')





if __name__ == '__main__':
    car = Car()
    car2 = Car()
    car.run()
    car2.run()
