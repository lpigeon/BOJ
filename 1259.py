import time

from numpy import result_type

st = time.time()

#a, b, c = map(int, input().split())
#a, b = map(int, sys.stdin.readline().rstrip().split())

from collections import Counter

import math
import itertools

import sys

while True:
    n = sys.stdin.readline().rstrip()
    if int(n) == 0:
        break
    
    reverse_n = "".join(list(reversed(list(n))))

    if int(n) == int(reverse_n):
        print("yes")
    else:
        print("no")

et = time.time()
print("time : {}".format(et-st))