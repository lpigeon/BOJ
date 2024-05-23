# 행렬 덧셈

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

a = [[0 for j in range(m)] for i in range(n)]
b = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    a[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    
for i in range(n):
    b[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    
result = [[(a[i][j] + b[i][j]) for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(result[i][j], end=' ')
    print()