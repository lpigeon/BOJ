# 세로읽기

import sys

m = []

for _ in range(5):
    n = list(map(str, sys.stdin.readline().rstrip()))
    if len(n) < 15:
        n += ['null'] * (15 - len(n))
    m.append(n)
    
result = ''

for i in range(15):
    for j in range(5):
        if m[j][i] == 'null':
            continue
        result += m[j][i]
        
print(result)