from unittest import TestCase
from Calc import Calc


class TestCalc1(TestCase):

    def testAdd1(self):
        num1 = 6
        num2 = 7
        sum = 13  # 期望

        calc = Calc()
        s = calc.add(num1, num2)  # 得到实际

        # 断言：
        self.assertEqual(s, sum)

    def testAdd2(self):
        num1 = -6
        num2 = -7
        sum = -13  # 期望

        calc = Calc()
        s = calc.add(num1, num2)  # 得到实际

        # 断言：
        self.assertEqual(s, sum)

    def testAdd3(self):
        num1 = -6
        num2 = 7
        sum = 1  # 期望

        calc = Calc()
        s = calc.add(num1, num2)  # 得到实际

        # 断言：
        self.assertEqual(s, sum)

    def testAdd4(self):
        num1 = 6
        num2 = -7
        sum = -1  # 期望

        calc = Calc()
        s = calc.add(num1, num2)  # 得到实际

        # 断言：
        self.assertEqual(s, sum)

    def testAdd5(self):
        num1 = 600000000000000000000000000000000000000000000000000000000000000000000000
        num2 = 7
        sum = 600000000000000000000000000000000000000000000000000000000000000000000007  # 期望

        calc = Calc()
        s = calc.add(num1, num2)  # 得到实际

        # 断言：
        self.assertEqual(s, sum)


class TestCalc2(TestCase):

    def testminus1(self):
        num1 = 18
        num2 = 10
        count = 8

        calc = Calc()
        c = calc.minus(num1, num2)

        self.assertEqual(c, count)

    def testminus2(self):
        num1 = -10
        num2 = -10
        count = 0

        calc = Calc()
        c = calc.minus(num1, num2)

        self.assertEqual(c, count)

    def testminus3(self):
        num1 = -8
        num2 = 10
        count = -18

        calc = Calc()
        c = calc.minus(num1, num2)

        self.assertEqual(c, count)

    def testminus4(self):
        num1 = 1800000000000000000000000000000000000000000000000000
        num2 = -10
        count = 1800000000000000000000000000000000000000000000000010

        calc = Calc()
        c = calc.minus(num1, num2)

        self.assertEqual(c, count)


class TestCalc3(TestCase):

    def testmulti1(self):
        num1 = 18
        num2 = 10
        count = 180

        calc = Calc()
        c = calc.multi(num1, num2)

        self.assertEqual(c, count)

    def testmulti2(self):
        num1 = -10
        num2 = -2
        count = 20

        calc = Calc()
        c = calc.multi(num1, num2)

        self.assertEqual(c, count)

    def testmulti3(self):
        num1 = 18
        num2 = -10
        count = -180

        calc = Calc()
        c = calc.multi(num1, num2)

        self.assertEqual(c, count)


class TestCalc4(TestCase):

    def testdevision1(self):
        num1 = 20
        num2 = 10
        count = 2

        calc = Calc()
        c = calc.devision(num1, num2)

        self.assertEqual(c, count)

    def testdevision2(self):
        num1 = -20
        num2 = 10
        count = -2

        calc = Calc()
        c = calc.devision(num1, num2)

        self.assertEqual(c, count)

    def testdevision3(self):
        num1 = -20
        num2 = -10
        count = 2

        calc = Calc()
        c = calc.devision(num1, num2)

        self.assertEqual(c, count)
