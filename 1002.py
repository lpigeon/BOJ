# 터렛

import math
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())

    r3 = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    max_r = max(r1, r2)
    min_r = min(r1, r2)

    if r3 == 0 and r1 == r2:
        print(-1)
    elif max_r > min_r+r3 or r3 > r1+r2:
        print(0)
    elif max_r == min_r+r3 or r3 == r1+r2:
        print(1)
    else:
        print(2)