# 마인크래프트
import time
st = time.time()

#a, b, c = map(int, input().split())
#a, b = map(int, sys.stdin.readline().rstrip().split())

from collections import Counter, deque
import sys
n, m, b= map(int, sys.stdin.readline().rstrip().split())
block_list = []
for _ in range(n):
    block_list.extend(list(map(int, sys.stdin.readline().rstrip().split())))
max_height = max(block_list)
redun = 0
blank = 0
total_time = 0
min_time = 1e9
result = []
 
# 높이 0부터 max_height 탐색
for h in range(max_height+1):
    for i in block_list:
        if i <= h:
            blank += h - i
        else:
            redun += i - h
    if blank > redun+b:
        continue
    # 걸린 시간 저장
    total_time += redun*2 + blank 
    # 현재까지 제일 적은 시간과 비교하여 적을경우 result값 업데이트
    if total_time <= min_time:
        result_time = total_time
        result_height = h
        min_time = total_time
    total_time = 0
    redun = 0
    blank = 0

print("{} {}".format(result_time, result_height))





et = time.time()
print("time : {:.4f}".format(et-st))