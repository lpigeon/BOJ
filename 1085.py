# 직사각형에서 탈출

import sys
x, y, w, h = map(int, sys.stdin.readline().rstrip().split())

result = min([x, w-x, y, h-y])
print(result)