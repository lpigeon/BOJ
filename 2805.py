import time
from tracemalloc import start

st = time.time()

#a, b, c = map(int, input().split())
#a, b = map(int, sys.stdin.readline().rstrip().split())

from collections import Counter, deque
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
tree_list = list(map(int, sys.stdin.readline().rstrip().split()))
tree_list.sort()

start = 0
end = tree_list[-1]

result = 0
while start <= end:
    total = 0
    mid = (start + end)//2
    for i in tree_list:
        if i > mid:
            total += i - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)















            
et = time.time()
print("time : {:.4f}".format(et-st))