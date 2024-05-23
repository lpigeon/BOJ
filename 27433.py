# 팩토리얼 2

import sys

n = int(sys.stdin.readline().rstrip())

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(n))