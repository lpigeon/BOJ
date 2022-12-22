import time

from numpy import result_type

st = time.time()

#a, b, c = map(int, input().split())
#a, b = map(int, sys.stdin.readline().rstrip().split())

from collections import Counter

import math
import itertools

import sys
l = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()
r = 31
M = 1234567891
total = 0

for i in range(l):
    total += (ord(s[i])-96)*(r**i)

H = total % M
print(H)



et = time.time()
print("time : {}".format(et-st))