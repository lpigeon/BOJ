from re import A
import time

from numpy import result_type

st = time.time()

#a, b, c = map(int, input().split())
#a, b = map(int, sys.stdin.readline().rstrip().split())

from collections import Counter

import math
import itertools

import sys
n = int(sys.stdin.readline().rstrip())
people = []
result = [1]*n
for i in range(n):
    w, h = map(int, sys.stdin.readline().rstrip().split())
    people.append([w,h])

for num, i in enumerate(people):
    for j in people:
        if i == j:
            continue
        elif i[0] < j[0] and i[1] < j[1]:
            result[num] += 1

for i in result:
    print("{}".format(i),end=" ")


et = time.time()
print("time : {}".format(et-st))