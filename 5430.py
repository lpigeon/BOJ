# AC

# deque의 장점을 잘 사용해야 하는 문제임
# deque는 popleft와 pop을 상수시간에 처리가능
# 따라서, R의 갯수의 따라 popleft와 pop을 적절히 써주고
# 마지막에 R을 청산해 주면 시간초과 없이 정답 가능

import sys
from collections import deque
t = int(sys.stdin.readline().rstrip())
reverseCount = 0

for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    x = sys.stdin.readline().rstrip()
    if x == "[]":
        x = deque()
    else:
        x = deque(x[1:-1].split(","))
    for i in p:
        if i == "R":
            reverseCount += 1
        elif i == "D":
            try:
                if reverseCount%2 == 1:
                    x.pop()
                else:
                    x.popleft()
            except:
                print("error")
                x.append("error")
                break
    if "error" not in x:
        if reverseCount%2 == 1:
            x.reverse()
        print("[{}]".format(",".join(x)))
    reverseCount = 0