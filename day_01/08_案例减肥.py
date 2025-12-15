
class Student:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self):
        self.weight += 2

    def run(self):
        self.weight -= 0.2




if __name__ == '__main__':
    xiaoming = Student('xiaoming', 100)
    xiaoming.run()
    print(xiaoming.weight)

    xiaoming.eat()
    print(xiaoming.weight)