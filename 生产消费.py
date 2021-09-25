from threading import Thread

import time

dan_ta = 500


class shengchan(Thread):
    username = ""
    count = 0

    def run(self) -> None:

        global dan_ta  # 使用全局变量
        while 1:  # 死循环
            if dan_ta < 500:
                self.count = self.count + 1
                dan_ta = dan_ta + 1
                print("还有", dan_ta, "蛋挞")
                time.sleep(0.01)
            elif dan_ta > 500:
                time.sleep(3)
                break
        print("总共制造了", dan_ta, "个蛋挞！")


class xiaofei(Thread):
    username = ""
    money = 3000
    count = 0

    def run(self) -> None:
        global dan_ta
        while 1:  # 死循环
            if self.money > 0 and dan_ta > 0:
                self.count = self.count + 1
                self.money = self.money - 2
                dan_ta = dan_ta - 1
                print(self.username, "买了", self.count, "个蛋挞！", "还剩", self.money)
                time.sleep(0.01)
            elif self.money == 0:
                print("没有钱了")
                print(self.username, "买了", self.count, "个蛋挞！")
                break
            elif dan_ta == 0:
                time.sleep(2)


u1 = shengchan()
u1.username = "少岩"

u2 = shengchan()
u2.username = "少安"

u3 = shengchan()
u3.username = "少承"

x1 = xiaofei()
x1.username = "少煜"

x2 = xiaofei()
x2.username = "少禹"

x3 = xiaofei()
x3.username = "少御"

x4 = xiaofei()
x4.username = "少楷"

x5 = xiaofei()
x5.username = "少旸"

x6 = xiaofei()
x6.username = "少疆"

u1.start()
u2.start()
u3.start()
x1.start()
x2.start()
x3.start()
x4.start()
x5.start()
x6.start()
