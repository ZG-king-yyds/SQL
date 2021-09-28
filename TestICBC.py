import xlrd
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from bank import bank
from ICBC import bank_addUser

wb = xlrd.open_workbook(filename=r"E:\PyCharm1\资料\day12\银行.xlsx")

bank = {}

# sheet = wb.sheet_by_index(0)  # 打开第一个选项卡

nsheet = wb.nsheets

for i in range(nsheet):
    st = wb.sheet_by_index(i)
    nrow = st.nrows

for username in bank:
    print(username)


#  username,password,country,province,street,door,money
da1 = [
    ["贾生", 123456, "USA", "纽约省", "桃园路", "s001", 3000, 1],
    ["贾生", 123456, "USA", "纽约省", "桃园路", "s001", 3000, 2]
]

da2 = [
    ["牛头", 456789, '地狱', '冥地', "阳泉路", "s002", 2000, 1]
]


@ddt
class TestICBC1(TestCase):

    @data(*da1)
    @unpack
    def testAdduser1(self, a, b, c, d, e, f, g, h):
        s = bank_addUser(a, b, c, d, e, f, g)
        self.assertEqual(s, h)


@ddt
class TestICBC2(TestCase):

    @data(*da2)
    @unpack
    def testAdduser2(self, a, b, c, d, e, f, g, h):
        s = bank_addUser(a, b, c, d, e, f, g)
        self.assertEqual(s, h)


data = st.row_values(1, st.nrows)
#
#
@ddt
class TestICBC3(TestCase):

    @data(*bank)
    @unpack
    def testAdduser2(self, username):
        n = bank()
        s = bank_addUser(username)
        self.assertEqual(s, n)
