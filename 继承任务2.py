class chushi:
    username = ""
    age = 0

    def setusername(self, username):
        self.username = username

    def getusername(self):
        return self.username

    def setage(self, age):
        if age > 150 or age < 0:
            print("年龄非法，重新输入！")
        else:
            return self.age

    def chaocai(self):
        print("徒弟年龄为", self.age, "的", self.username, "开始炒菜")

    def zhengfan(self):
        print("徒孙年龄为", self.age, "的", self.username, "开始蒸饭")


class tudi(chushi):
    car = ""
    address = ""

    def chaocai(self):
        super().chaocai()
        print("徒弟开",self.car,"去",self.address)



class tusun(tudi):

    def zhengfan(self):
        super().zhengfan()


tudi = tudi()
tudi.username = "徒弟"
tudi.age = 40
tudi.address = "巴黎"
tudi.car = "阿斯顿马丁"
tudi.chaocai()

tusun = tusun()
tudi.username = "徒孙"
tudi.age = 50
tudi.zhengfan()
