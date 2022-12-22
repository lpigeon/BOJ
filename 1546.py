# 평균 

import sys

new_arr = []
total = 0
n = int(sys.stdin.readline().rstrip())
arr = list(sys.stdin.readline().rstrip().split())
arr = [int (i) for i in arr]
maxPoint = max(arr)

for i in range(n):
    new_arr.append(arr[i]/maxPoint*100)
    total = total + new_arr[i]
print(total/n)