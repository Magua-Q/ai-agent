


class Car:
    def run(self):
        print("汽车会跑。。。")

    def work(self):
        self.run()

if __name__ == '__main__':
    car = Car()
    car.run()
    print('__' * 22)
    car.work()