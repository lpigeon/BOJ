#반례만드는데 쓴 코드
from random import randint

H = randint(8,50)
W = randint(8,50)
RowList = []

for y in range(H):
    Temp = ''
    for x in range(W):
        random = randint(0,1)
        if random == 0:
            Temp += 'W'
        else:
            Temp += 'B'
    RowList.append(Temp)