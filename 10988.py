# 팰린드롬인지 확인하기

import sys

n = sys.stdin.readline().strip()

if n == n[::-1]:
    print(1)
else:
    print(0)