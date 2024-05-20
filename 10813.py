# 공 바꾸기

import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().rstrip().split())

n_list = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())

    n_list[i-1] , n_list[j-1] = n_list[j-1], n_list[i-1]

for i in n_list:
    print("{}".format(i),end=" ")
