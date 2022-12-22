# 동전 0

# 그리디 알고리즘 사용
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coin = []
count = 0
for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))
coin.reverse()
for i in coin:
    if k < i:
        continue
    count += k//i
    k -= (k//i)*i
    if k == 0:
        break
    
print(count)