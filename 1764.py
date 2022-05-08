# 듣보잡

# set 교집합 사용
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
notListen = []
notSee = []

for _ in range(n):
    notListen.append(sys.stdin.readline().rstrip())
for _ in range(m):
    notSee.append(sys.stdin.readline().rstrip())
    
result = list(set(notListen)&set(notSee))
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])