# 개수 세기

import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())

n_list = list(map(int, sys.stdin.readline().rstrip().split()))

v = int(sys.stdin.readline().rstrip())

counter= Counter(n_list)
print(int(counter[v]))

