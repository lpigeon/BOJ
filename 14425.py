# 문자열 집합

import sys

def binary_search(target, data):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return 0

n, m = map(int, sys.stdin.readline().rstrip().split())
s = []
f = []
for _ in range(n):
    s.append(sys.stdin.readline().rstrip())
for _ in range(m):
    f.append(sys.stdin.readline().rstrip())
    
s.sort()
count = 0
for i in f:
    count += binary_search(i, s)
print(count)