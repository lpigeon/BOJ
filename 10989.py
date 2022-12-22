import time
st = time.time()

#a, b, c = map(int, input().split())
#a, b = map(int, sys.stdin.readline().rstrip().split())

from collections import Counter, deque
import sys

cslist = [0 for _ in range(10001)]

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    cslist[num] += 1

for i in range(1, 10001):
    count = cslist[i]
    for _ in range(count):
        print(i)

        
et = time.time()
print("time : {:.4f}".format(et-st))