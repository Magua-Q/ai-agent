class Phone:
    def open(self):
        print("手机开机")

    def close(self):
        print("手机关机")

    def take_photo(self):
        print("手机拍照")


if __name__ == '__main__':

    apple = Phone()
    apple.open()
    apple.close()
    apple.take_photo()
    apple.open()
