import csv
import json
with open('STOCK_DAY_2330_202109.csv', encoding='UTF-8') as csv_file:
    rd = csv.reader(csv_file)
    head = None
    L = []
    a = 0   # 成交金額加總
    b= 0    # 收盤價加總
    for row in rd:
        if head is None:
            head = [row[0], row[2], row[6]]
        else:
            row[2] = int(row[2].replace(",", ""))
            row[6] = int(row[6].replace(",", ""))
            L += [{str(head[0]):row[0], str(head[1]):row[2], str(head[2]):row[6]}]
            a += row[2]
            b += row[6]
# print(L)
for row in L:
    print(row)
# print 平均價
print('平均成交金額 = ', a/len(L))
print('平均收盤價 = ', b/len(L))

# print(L2)
L2 = sorted(L, key = lambda L : L['成交金額'])
for row in L2:
    print(row)
    
# 匯入jason檔
with open('L2.json', 'w') as jFile:
    json.dump(L2, jFile)

# 確認是否成功匯入
with open('L2.json') as jFile:
    jData = jFile.read()
    d = json.loads(jData)
if d == L2 :
    print('成功匯入')