# 참외밭

import sys

k = int(sys.stdin.readline().rstrip())

fieldList = []

for _ in range(6):
    _, l = map(int, sys.stdin.readline().rstrip().split())
    fieldList.append(l)
x = max(fieldList[0], fieldList[2], fieldList[4])
y = max(fieldList[1], fieldList[3], fieldList[5])
temp = fieldList.copy()
temp2 = fieldList.copy()
xIndex = fieldList.index(x)
temp[xIndex] = 0
yIndex = temp.index(y)

index = [xIndex, yIndex]
n = []
maxIndex = max(index)
for i in temp2:
    fieldList.append(i)
count = 0
for i in fieldList[maxIndex+1:-1]:
    if count == 1 or count == 2:
        n.append(i)
    count += 1
    if count > 3:
        break
nx = n[0]
ny = n[1]
area = x*y - nx*ny
print(k*area)