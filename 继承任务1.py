import time


class Oldphone:
    username = ""
    band = ""
    lingsheng = ""
    address = ""

    def setusername(self, username):
        self.username = username

    def getusername(self):
        return self.username

    def setband(self, band):
        self.band = band

    def getband(self):
        return self.band

    def dadianhua(self, name):
        print(self.username, "正在用", self.band, "手机给", name, "打电话")

    def call(self):
        print("语音拨号中，地址为", self.address)
        for i in range(8):
            print(".", end="")
            time.sleep(1)
        print("正在给", self.username, "打电话","铃声为",self.lingsheng)
        print(self.band,"品牌的手机很好用")


class Xinphone(Oldphone):

    def cell(self, username):
        super().call(username)  # 引用父类


old = Oldphone()
old.band = "OPPO Reno"
old.username = "降尘"
old.dadianhua("将臣")

xin = Xinphone()
xin.address = "广州"
xin.band = "vivo NEX"
xin.username = "江川"
xin.lingsheng = "星月为媒"
xin.call()


