# 킹, 퀸, 룩, 비숍, 나이트, 폰

import sys

n = list(map(int, sys.stdin.readline().split()))

print(1 - n[0], 1 - n[1], 2 - n[2], 2 - n[3], 2 - n[4], 8 - n[5])