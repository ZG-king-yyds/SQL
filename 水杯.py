class shuibei:
    __height = 0
    __rongji = 0
    __color = ""
    __caizhi = ""

    # def __setheight(self, height):
    #     self.__height = height
    #
    # def getheight(self):
    #     return self.__height

    def __setrongji(self, rongji):
        self.__rongji = rongji

    def getrongji(self):
        return self.__rongji

    def cun(self, rongji):
        print("能存放的液体容积为:", rongji, "升")


sb = shuibei()
sb.cun(200)
