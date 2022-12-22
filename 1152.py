# 단어의 개수

import sys
from collections import Counter
s = sys.stdin.readline().rstrip().split()
s = Counter(s)
print(sum(s.values()))