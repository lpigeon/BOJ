# 구간 합 구하기 4

import sys
import itertools

n, m = map(int, sys.stdin.readline().rstrip().split())

nList = list(map(int, sys.stdin.readline().rstrip().split()))
result = list(itertools.accumulate(nList))
for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    if i == j:
        print(nList[i-1])
    else:
        print(result[j-1] - result[i-1] + nList[i-1])
    
    