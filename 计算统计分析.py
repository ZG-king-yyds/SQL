import xlrd

clothes = {}
wb = xlrd.open_workbook(filename=r"E:\PyCharm1\资料\day7\excle/2020年每个月的销售情况.xlsx")
month = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
sum = 0
sum1 = 0
for a in range(0, 12):
    sheet = wb.sheet_by_name(month[a])
    rows = sheet.nrows
    cols = sheet.ncols
    for q in range(1, rows):
        data = sheet.row_values(q)
        sum = sum + data[2] * data[4]
print("衣服年总销售额为：", round(sum, 2))

for a in range(0, 12):
    sheet = wb.sheet_by_name(month[a])
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(1, rows):
        data = sheet.row_values(i)
        sum1 = sum1 + data[4]
print("衣服年总销售量为：", round(sum1))
print("-----------------------------")

for a in range(0, 12):
    sheet = wb.sheet_by_name(month[a])
    rows = sheet.nrows
    cols = sheet.ncols
    for m in range(1, rows):
        data = sheet.row_values(m)
        if data[1] in clothes:
            clothes[data[1]] = clothes[data[1]] + data[4]
        else:
            clothes[data[1]] = data[4]
        for i in clothes.keys():
            bi = clothes[i] / sum1

print("每种衣服一年的销售量分别为：", clothes)
print("每种衣服销售量占比：")
for i in clothes:
    print(i, round(clothes[i] / sum1 * 100, 2), "%")
print("-----------------------------")
# for k in clothes:
s = max(clothes.values())
print("全年最畅销衣服的数量：")
print(round(s))
print("-----------------------------")
# for j in clothes:
d = min(clothes.values())
print("全年销售量最低衣服的数量：")
print(round(d))
print("-----------------------------")
for a in range(0, 12):
    sheet = wb.sheet_by_name(month[a])
    rows = sheet.nrows
    cols = sheet.ncols
    for m in range(1, rows):
        data = sheet.row_values(m)
        if data[1] in clothes:
            clothes[data[1]] = clothes[data[1]] + data[2] * data[4]
        else:
            clothes[data[1]] = data[2] * data[4]
print("每种衣服一年的销售额分别为：", clothes)
print("每种衣服销售额占比：")
for i in clothes:
    print(i, round(clothes[i] / sum * 100, 2), "%")
print("-----------------------------")



