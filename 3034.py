# 앵그리 창영
import sys
import math
n, w, h = map(int, sys.stdin.readline().rstrip().split())
minLen = min(w,h)
c = math.sqrt(w**2 + h**2)

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x<=c:
        print("DA")
    else:
        print("NE")
