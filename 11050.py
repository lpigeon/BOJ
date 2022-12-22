import time

from numpy import result_type

st = time.time()

#a, b, c = map(int, input().split())
#a, b = map(int, sys.stdin.readline().rstrip().split())

from collections import Counter

import math
import itertools

import sys

import math
n, k = map(int, input().split())
print(math.comb(n,k))

et = time.time()
print("time : {}".format(et-st))