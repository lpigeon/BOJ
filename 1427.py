# 소트인사이드

import sys

n = list(sys.stdin.readline().rstrip())
n = [int(i) for i in n]
n.sort(reverse=True)
n = [str(i) for i in n]
print("".join(n))