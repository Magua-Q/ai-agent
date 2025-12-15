class Digua:
    def __init__(self):
        self.status = "生"
        self.cook_time = 0
        self.condiments = []


    def cook(self, time):
        if time < 0:
            print("时间有误")
        else:
            self.cook_time += time
            if 0 <= self.cook_time < 3:
                self.status = '生'
            elif 3 <= self.cook_time < 6:
                self.status = '半熟'
            elif 6 <= self.cook_time < 8:
                self.status = '熟'
            else:
                self.status = '焦了'

    def add_condiment(self, condiment):
        self.condiments.append(condiment)


    def __str__(self):
        return f"地瓜烘烤时间: { self.cook_time }; 地瓜烘烤状态：{ self.status}"


if __name__ == '__main__':
    digua = Digua()
    digua.cook(3)
    digua.cook(6)
    digua.cook(7)
    digua.cook(8)
    print(digua)

