# 숫자 카드

import sys

def binary_search_recursion (target, start, end, data):
    if start > end:
        return 0
    mid = (start + end) // 2
    if data[mid] == target:
        return 1
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1        
    return binary_search_recursion(target, start, end, data)

n = int(sys.stdin.readline().rstrip())
nList = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
mList = list(map(int, sys.stdin.readline().rstrip().split()))

nList.sort()
for i in mList:
    print(binary_search_recursion(i,0,len(nList)-1,nList), end=" ")
