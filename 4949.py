import time
st = time.time()

#a, b, c = map(int, input().split())
#a, b = map(int, sys.stdin.readline().rstrip().split())

from collections import Counter, deque
import sys

bstack = []

while True:
    s = sys.stdin.readline().rstrip()
    if s == ".":
        break
    for i in s:
        if i == "(":
            bstack.append(i)
        elif i == ")":
            if len(bstack) == 0:
                bstack.append(i)
                break
            elif bstack[-1] != "(":
                break
            bstack.pop()
        elif i == "[":
            bstack.append(i)
        elif i == "]":
            if len(bstack) == 0:
                bstack.append(i)
                break
            elif bstack[-1] != "[":
                break
            bstack.pop()
    if len(bstack) == 0:
        print("yes")
    else:
        print("no")
    bstack = []

    
et = time.time()
print("time : {:.4f}".format(et-st))