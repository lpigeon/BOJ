# 비밀번호 찾기

import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
memo = {}

for _ in range(n):
    site, pw = map(str, sys.stdin.readline().rstrip().split())
    memo[site] = pw
for _ in range(m):
    targetSite = sys.stdin.readline().rstrip()
    print(memo[targetSite])