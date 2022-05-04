# 좌표 압축
import time

from numpy import result_type

st = time.time()

#a, b, c = map(int, input().split())
#a, b = map(int, sys.stdin.readline().rstrip().split())

from collections import Counter
import sys

n = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
result = {}
sort_num_list = sorted(num_list)
comp = sort_num_list[0]
x = 0

for i in sort_num_list:
    if comp < i:
        x += 1
        result[i] = x
        comp = i
    else:
        result[i] = x

for i in num_list:
    print("{}".format(result[i]), end=" ")









et = time.time()
print("time : {}".format(et-st))