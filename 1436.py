import time
st = time.time()

#a, b, c = map(int, input().split())
#a, b = map(int, sys.stdin.readline().rstrip().split())

from collections import Counter, deque
import sys
n = int(sys.stdin.readline().rstrip())
result = 666
count = 1
while True:
    if n == count:
        print(result)
        break
    result += 1
    if "666" in str(result):
        count += 1
    
et = time.time()
print("time : {:.4f}".format(et-st))