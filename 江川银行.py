'''import time
print("系统正在加载\n" ,end="")
for i in range(3):
    print("...\n", end="")
    time.sleep(0.5)'''
print("                   江川银行欢迎您                      ")
print("|------------1、开户                     ------------|")
print("|------------2、取钱                     ------------|")
print("|------------3、存钱                     ------------|")
print("|------------4、转账                     ------------|")
print("|------------5、查询                     ------------|")
print("|------------6、退出                     ------------|")
print("=====================================================")
import random
import pymysql

# 连接
con = pymysql.connect(host='localhost', user='root', password='', database='company')
# 创建控制台
cursor = con.cursor()
bank = {}  # 创建一个空的字典
# 开户逻辑
bank_name = "江川银行"


# 第一个对应第一个 不是名称对应名称
def bank_adduser(account, username, password, country, province, street, door, money):
    sql = "select * from  bank"
    cursor.execute(sql)
    bank = cursor.fetchall()
    if len(bank) > 100:
        return 3
    if account in bank:  # 如变量在容器内执行下面的代码
        return 2
    return 1


def adduser():  # 定义了一个方法
    username = input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    money = input("\t\t请输入您的余额")
    account = random.randint(10000000, 99999999)
    stast = bank_adduser(account, username, password, country, province, street, door, money)
    #        调用方法   （元素，，，，，，，，，）
    if stast == 3:
        print("你去别的银行吧")
    elif stast == 2:
        print("开户失败，你别重复")
    elif stast == 1:
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, money, bank_name))
        sql = "insert into bank value (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param = [account, username, password, country, province, street, door, money, bank_name]
        cursor.execute(sql, param)
        con.commit()



# 3.存钱
def addmoney():  # 定义了一个方法
    account = input("请输入您的账户")
    sql = "select * from  bank where %s"
    param = account
    cursor.execute(sql, param)
    bank = cursor.fetchall()
    if len(bank) != 0:
        money = "select money from bank where %s"
        param = (account)
        cursor.execute(money, param)
        money1 = (input("请输入存取金额：￥"))
        sql = "update bank set money=money+%s where account=%s"
        param1 = (money1, account)
        cursor.execute(sql, param1)
        con.commit()
        # print("当前余额：￥", money)
        print("存款成功")
    else:
        print("账号不存在。请检查账户输入")
        return False


# 2.取钱
def qumoney():  # 定义了一个方法
    account = input("请输入您的账户")
    sql = "select * from  bank where %s"
    param = account
    cursor.execute(sql, param)
    bank = cursor.fetchall()
    if len(bank) != 0:
        password = input("请输入您的密码")
        sql1 = "select * from  bank where %s"
        param1 = password
        cursor.execute(sql1, param1)
        bank1 = cursor.fetchall()
        if len(bank1) != 0:
            money2 = (input("请取出金额：￥"))
            sql2 = "select money from  bank where account=%s"
            param2 = account
            cursor.execute(sql2, param2)
            bank2 = cursor.fetchall()
            money = bank2[0][0]
            money = int(money) - int(money2)
            if money < 0:
                print("余额不足")
            else:
                print("取钱成功")
                print("当前余额：￥", money)
                sql3 = "update bank set money=%s where account=%s"
                param3 = (money, account)
                cursor.execute(sql3, param3)
                con.commit()
        else:
            print("密码错误，请检查密码输入")
    else:
        print("账号不存在。请检查账户输入")
        return False


# 转账
def zz():
    account1 = int(input("请输入转出的账号"))
    account2 = int(input("请输入转入的账号"))
    sql = "SELECT * FROM  bank WHERE account=%s OR  account=%s"
    param = account1, account2
    cursor.execute(sql, param)
    bank = cursor.fetchall()
    if len(bank) == 2:
        password = input("请输入转出的账号密码")
        sql1 = "select * from  bank where %s"
        param1 = password
        cursor.execute(sql1, param1)
        bank1 = cursor.fetchall()
        if len(bank1) != 0:
            sql2 = "select money from  bank where account=%s"
            param2 = account1
            cursor.execute(sql2, param2)
            bank2 = cursor.fetchall()
            money = bank2[0][0]
            money = int(money)
            print("当前余额为￥", money)
            money1 = int(input("请输入转账金额：￥"))
            if money1 <= money:
                # money  -= money
                sql1 = "update bank set money=money-%s where account=%s"
                param1 = (money1, account1)
                cursor.execute(sql1, param1)
                con.commit()
                sql2 = "update bank set money=money+%s where account=%s"
                param2 = (money1, account2)
                cursor.execute(sql2, param2)
                con.commit()
                # money3 += money
                print("转账成功！")
        else:
            print("密码错误，请检查密码输入")
    else:
        print("账号不存在。请检查账户输入")


# 查询功能
def cha():
    caccount = int(input("请输入想要查询的账号："))
    sql = "select * from  bank where %s"
    param = caccount
    cursor.execute(sql, param)
    bank = cursor.fetchall()
    if len(bank) != 0:
        password = input("请输入密码：")
        sql1 = "select * from  bank where %s"
        param1 = password
        cursor.execute(sql1, param1)
        bank1 = cursor.fetchall()
        if len(bank1) != 0:
            # print(" 用户名 账户 密码 国籍 省份 街道 门牌号  余额 开户行名称")
            sql2 = "select * from  bank where account=%s"
            param2 = caccount
            cursor.execute(sql2, param2)
            bank2 = cursor.fetchall()
            # for i in bank2 :
            #   print(i)
            info = '''
            用户名:%s
            账号：%s
            密码：%s
            国籍：%s
            省份：%s
            街道：%s
            门牌号：%s
            余额：%s
            开户行名称：%s
            '''
            print(info % (
            bank2[0][0], bank2[0][1], bank2[0][2], bank2[0][3], bank2[0][4], bank2[0][5], bank2[0][6], bank2[0][7],
            bank2[0][8],))
        else:
            print("密码错误，请检查密码输入")
    else:
        print("账号不存在。请检查账户输入")


while True:
    begin = input("请选择业务")
    if begin == "1":
        adduser()
    elif begin == "2":
        qumoney()
    elif begin == "3":
        addmoney()
    elif begin == "4":
        zz()
    elif begin == "5":
        cha()
    else:
        print("拜拜了您嘞")
        break
cursor.close()
con.close()
