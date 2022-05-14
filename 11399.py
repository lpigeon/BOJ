# ATM

import sys
import itertools

n = int(sys.stdin.readline().rstrip())
p = list(map(int, sys.stdin.readline().rstrip().split()))
p.sort()

result = sum(itertools.accumulate(p))
print(result)