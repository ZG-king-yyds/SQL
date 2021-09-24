class people:
    username = ""
    sax = ""
    age = 0

    def ganhuo(self):
        print(self.username, "今年已经", self.age, "岁了", "性别", self.sax, "他开始干活了")

    def learn(self, xuehao):
        print(self.username, "今年的年龄为", self.age,"性别",self.sax, "学号为", xuehao, "他在认真学习")

    def sing(self, xuehao):
        print(self.username, "今年的年龄为", self.age,"性别", self.sax,"学号为", xuehao, "他在努力唱歌")


class gongren(people):

    def ganhuo(self):
        super().ganhuo()


class student(people):
    xuehao = ""

    def learn(self):
        super().learn()

    def sing(self):
        super().sing()


g = gongren()
g.username= "小李子"
g.sax = "男"
g.age = 40
g.ganhuo()

p = people()
p.username = "小明"
p.sax = "男"
p.age = 20
p.learn("20210304001")

p = people()
p.username = "小张"
p.sax = "男"
p.age = 21
p.sing("20210304002")