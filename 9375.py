# 패션왕 신해빈
import sys
from collections import Counter

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    clothes = []
    result = 1
    for _ in range(n):
        cloth = list(sys.stdin.readline().rstrip().split())
        clothes.append(cloth[1])
    count = list(Counter(clothes).values())
    for i in range(len(count)):
        temp = count[i]+1
        result *= temp
    print(result-1)