# Four Squares

import sys
n = int(sys.stdin.readline().rstrip())

dp = [0]*50001

for i in range(1,n+1):
    result = []
    j = 1
    while i >= j**2:
        result.append(dp[i-j**2])
        j += 1
    dp[i] = min(result)+1
print(dp[n])

