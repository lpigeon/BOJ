# 1로 만들기

import sys

n = int(sys.stdin.readline().rstrip())

dp = [0]*10000001

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[n])