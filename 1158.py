# 요세푸스 문제

import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
def josephus(n, k):
    live = [1]*(n+1)    
    live[0] = 0
    result = []
    x = 1
    for i in range(n-1):
        c = 1
        t = (k-1) % (n-i) + 1
        prev = len(result)            
        while len(result) == prev:   
            if live[x] == 1:
                if c == t:
                    live[x] = 0
                    result.append(x)
                c += 1
            x += 1
            if x == n+1:
                x = 1
    last = live.index(1)    
    result.append(last)
    return result

result = josephus(n, k)
print("<",end="")
for i in result:
    if i == result[-1]:
        print(i,end="")
        break
    print(i,end=", ")
print(">")