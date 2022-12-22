# 분수찾기

n = int(input())
i = 0
lenth = 0

while True:
    i += 1
    lenth += i
    if n <= lenth:
        break


if i % 2 == 0:
    for j in range(0,lenth+1):
        if j == lenth - n:
            print("{}/{}".format(i-j,1+j))
            break 
else:
    for j in range(0,lenth+1):
        if j == lenth - n:
            print("{}/{}".format(1+j,i-j))
            break 
