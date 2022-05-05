# 한수

import sys

n = sys.stdin.readline().rstrip()
count = 0

for n in range(1,int(n)+1):
    n = str(n)
    if len(n) == 1 or len(n) == 2:
        count = count + 1
    else:
        s1 = int(n[0]) - int(n[1])
        s2 = int(n[1]) - int(n[2])
        if s1 == s2:
            count = count + 1
print(count)