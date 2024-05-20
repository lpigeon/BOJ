# 공 넣기

import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().rstrip().split())

n_list = [0] * n

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().rstrip().split())
    
    for idx in range(i-1, j):
        n_list[idx] = k
            
for i in n_list:
    print("{}".format(i),end=" ")
