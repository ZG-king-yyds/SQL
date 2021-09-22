class Computer:
    __username = ""
    __big = 0
    __money = 0
    cpu = ""
    neicun = 0
    daijitime = 0

    def setusername(self, username):
        self.__username = username

    def getusername(self):
        return self.__username

    def dazi(self, username, time):
        print(username, "正在打字，已经打了", time, "个小时了")

    def playgame(self, username, time, gamename):
        print(username, "正在打游戏,已经打了", time, "个小时了，打的游戏是", gamename)

    def movie(self, username, time, moviename):
        print(username, "正在看电视剧,已经看了", time, "个小时了，看的是", moviename)


c = Computer()
c.dazi("张三", 2)
c.playgame("小明", 2, "和平精英")
c.movie("小小", 5, "我们的新时代")
