import time
st = time.time()

#a, b, c = map(int, input().split())
#a, b = map(int, sys.stdin.readline().rstrip().split())

from collections import Counter, deque
import sys
t = int(sys.stdin.readline().rstrip())
cnt = 0
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    printer = deque(list(map(int, sys.stdin.readline().rstrip().split())))

    while m != -1:
        max_prior = max(printer)
        if printer[0] != max_prior:
            temp = printer.popleft()
            printer.append(temp)
            if m != 0:
                m -= 1
            elif m == 0:
                m = len(printer) - 1
        elif printer[0] == max_prior:
            printer.popleft()
            if m != 0:
                m -= 1
                cnt += 1
            elif m == 0:
                m = -1
                cnt += 1
    print(cnt)
    cnt = 0



            
et = time.time()
print("time : {:.4f}".format(et-st))