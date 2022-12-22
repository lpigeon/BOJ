# 단어 공부
import sys
from collections import Counter
s = sys.stdin.readline().rstrip()
s = s.upper()
count = Counter(s)
maxNum = max(count.values())
if len([i for i in count.values() if i >= maxNum]) != len(set([i for i in count.values() if i >= maxNum])):
    print("?")
else:
    print(count.most_common()[0][0])