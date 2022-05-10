# 1,2,3 더하기 

import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    dp = [0]*12
    dp[0] = 1
    dp[1] = 2
    dp[2] = 3
    
    
    
    print(dp[n])
       