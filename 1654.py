import time
st = time.time()

#a, b, c = map(int, input().split())
#a, b = map(int, sys.stdin.readline().rstrip().split())

from collections import Counter, deque
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
lan_list = []
for _ in range(n):
    lan_list.append(int(sys.stdin.readline().rstrip()))
lan_list.sort()

start = 0
end = lan_list[-1]

result = 0
while start <= end:
    total = 0
    mid = (start + end)//2
    if mid <= 0: #같은 길이로 자르는 것도 포함되어야 하므로
        result = 1
        break
    for i in lan_list:
        if i >= mid:
            total += i//mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

    
et = time.time()
print("time : {:.4f}".format(et-st))