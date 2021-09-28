import pymysql
import xlrd


class ExcelToSqlite(object):
    exe = "   执行: "
    output = "   输出： "
    sheetDataStartIndex = 1  # 数据开始计算的行数，如第o行是表头，第1行及之后是数据

    def __init__(self, dbName):
        print("初始化数据库实例")
        super(ExcelToSqlite, self).__init__()
        self.conn = pymysql.connect(dbName)
        self.cursor = self.conn.cursor()

    def __del__(self):
        print("释放数据库实例")
        self.cursor.close()
        self.conn.close()

    def ExcelToDb(self, excelName, sheetIndex, tableName):
        '''

        excel转化为mysql数据库表
        :param excelName:12月份提付销售数据.xlsx
        :param sheetIndex:excel中sheet位置
        :param tableName:clothes
        '''

        print("Excel文件 转 db")
        self.tableName = tableName
        excel = xlrd.open_workbook(excelName)
        sheet = excel.sheets()[sheetIndex]  # sheets 索引
        self.sheetRows = sheet.nrows  # excel 行数
        self.sheetCols = sheet.ncols  # excel 列数
        filedNamess = sheet.row_values(0)  # 得到表头字段名
        # 创建表
        filedTypes = ""
        for index in range(filedNamess.__len__()):
            if index != filedNamess.__len__() - 1:
                filedTypes += filedNamess[index] + " text,"
            else:
                filedTypes += filedNamess[index] + " text"
        self.__CreateTable(tableName, filedTypes)
        # 插入数据
        for rowId in range(self.sheetDataStartIndex, self.sheetRows):
            filedValues = sheet.row_values(rowId)
            self.__Insert(filedNamess, filedValues)

        def __CreateTable(self, tableName, field):
            '''

            创建表
            :param tableName:表名
            :param field: 字段名类型
            :return:
            '''

            print("创建表" + tableName)
            sql = 'create table if not exists %s(%s)' % (self.tableName, field)  # primary key not null
            print(self.exe + sql)
            self.cursor.execute(sql)
            self.conn.commit()

        def __Insert(self, fieldNames, fieldValues):
            """
            插入数据
            :param fieldNames: 字段list
            :param fieldValues: 值list
            """
            # 通过fieldNames解析出字段名
            names = ""  # 字段名，用于插入数据
            nameTypes = ""  # 字段名及字段类型，用于创建表
            for index in range(fieldNames.__len__()):
                if index != fieldNames.__len__() - 1:
                    names += fieldNames[index] + ","
                    nameTypes += fieldNames[index] + " text,"
                else:
                    names += fieldNames[index]
                    nameTypes += fieldNames[index] + " text"
            # 通过fieldValues解析出字段对应的值
            values = ""
            for index in range(fieldValues.__len__()):
                cell_value = str((fieldValues[index]))
                if isinstance(fieldValues[index], float):
                    cell_value = str((int)(fieldValues[index]))  # 读取的excel数据会自动变为浮点型，这里转化为文本
                if index != fieldValues.__len__() - 1:
                    values += "\'" + cell_value + "\',"
                else:
                    values += "\'" + cell_value + "\'"
            # 将fieldValues解析出的值插入数据库
            sql = 'insert into %s(%s) values(%s)' % (self.tableName, names, values)
            print(self.exe + sql)
            self.cursor.execute(sql)
            self.conn.commit()

        def Query(self, tableName):
            """
            查询数据库表中的数据
            :param tableName:表名
            """
            print("查询表 " + tableName)
            sql = 'select * from %s' % (tableName)
            print(self.exe + sql)
            self.cursor.execute(sql)
            results = self.cursor.fetchall()  # 获取所有记录列表
            index = 0
            for row in results:
                print(self.output + "index=" + index.__str__() + " detail=" + str(row))  # 打印结果
                index += 1
            print(self.output + "共计" + results.__len__().__str__() + "条数据")

        def executeSqlCommand(self, sqlCommand):
            """
            执行输入的sql命令
            :param sqlCommand: sql命令
            """
            print("执行自定义sql " + tableName)
            print(self.exe + sqlCommand)
            self.cursor.execute(sqlCommand)
            results = self.cursor.fetchall()
            print(self.output + str(results))
            for index in range(0, results.__len__()):
                print(self.output + str(results[index]))
            self.conn.commit()

        dbName = "/Users/amarao/Public/workspace/db workspace/mydb"  # 数据库名,数据库不存在会自动创建，路径不存在会执行失败
        tableName = "colthes"  # 数据库表名，表存不存在都可以
        excelName = "E:\PyCharm1\资料\day7\excle\12月份衣服销售数据.xlsx"  # excel名(可加路径)

        es = ExcelToSqlite(dbName)
        es.ExcelToDb(excelName, 0, tableName)
        es.Query(tableName)
        es.executeSqlCommand("select * from " + tableName)
