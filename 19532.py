# 수학은 비대면강의입니다

import sys
from collections import Counter

a, b, c, d, e, f = map(int, sys.stdin.readline().rstrip().split())

x, y = -999, -999

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a*i + b*j == c and d*i + e*j == f:
            x, y = i, j
            break
    if x != -999:
        break

print(x, y)