# 최댓값

import sys

m = []

for _ in range(9):
    n = list(map(int, sys.stdin.readline().rstrip().split()))
    m.append(n)

max_value = -1
for i in range(9):
    for j in range(9):
        if m[i][j] > max_value:
            x = i
            y = j
            max_value = m[i][j]
            
print(max_value)
print(x + 1, y + 1)