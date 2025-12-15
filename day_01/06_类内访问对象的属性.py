

class Car:
    def show(self):
        print(f"颜色: { self.color}")
        print(f"轮胎数：{ self.nums}")



if __name__ == '__main__':
    car = Car()
    car.color = 'red'
    car.nums = 4

    car.show()