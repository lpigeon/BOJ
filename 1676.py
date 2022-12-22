# 팩토리얼 0의 개수

import sys

def facto(n):
    if n == 0:
        return 1
    return n*facto(n-1)

n = int(sys.stdin.readline().rstrip())
nList = list(str(facto(n)))
zeroCount = 0
while True:
    isZero = nList.pop()
    if isZero == "0":
        zeroCount += 1
    else:
        break
print(zeroCount)