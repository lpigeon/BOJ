# 영수증

import sys


x = int(sys.stdin.readline().rstrip())

n = int(sys.stdin.readline().rstrip())

a_list = []
b_list = []

sum = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    a_list.append(a)
    b_list.append(b)
    
for b in b_list:
    sum += a_list[0] * b
    a_list.pop(0)

if x == sum:
    print("Yes")
else:
    print("No")