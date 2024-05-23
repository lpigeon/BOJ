# 알고리즘 수업 - 피보나치 수 1

import sys

n = int(sys.stdin.readline().rstrip())

a, b = 0, 0

def fib(n):
    global a
    if n == 1 or n == 2:
        a += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
def fibonacci(n):
    global b
    f = [0, 1, 1]
    for i in range(2, n):
        b += 1
        f.append(f[i] + f[i - 1])
    return f[n]

fib(n)
fibonacci(n)

print(a, b)