# 과제 안 내신 분..?

import sys
from collections import Counter

n = 30

n_list = [i for i in range(1, n+1)]

for _ in range(n-2):
    i = int(sys.stdin.readline().rstrip())
    n_list[i - 1] = 0

for i in n_list:
    if i:
        print("{}".format(i))
