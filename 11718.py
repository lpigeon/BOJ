# 그대로 출력하기

import sys

for _ in range(100):
    try:
        n = sys.stdin.readline().strip()
        print(n)
    except EOFError:
        break

