# 리모컨

import time
st = time.time()

from collections import Counter
import sys
import itertools

# 반례가 많음. 조건을 잘따져야 함.
n = sys.stdin.readline().rstrip()
m = int(sys.stdin.readline().rstrip())
if m != 0:
    brokenNum = list(map(int, sys.stdin.readline().rstrip().split()))
    allNum = [int(x) for x in range(10)]
    usableNum = list(map(str, set(allNum) - set(brokenNum)))
resultSub = 1e9

# n이 100이면 다른 조건에 상관없이 버튼을 안눌러도 되므로 0
if int(n) == 100:
    print(0)
elif m == 0:
    # m이 존재하는데 n이 100이어도 버튼을 안눌러도 되므로 0
    if int(n) == 100:
        print(0)
    # 위 조건이 아닐 시, 버튼을 눌러서 채널을 돌리는 방법과 +,- 를 눌러
    # 돌리는 방법 중 더 최적의 방법 출력
    else:
        m0Count = len(n)
        compm0Count = abs(int(n)-100)
        if m0Count < compm0Count:
            print(m0Count)
        else:
            print(compm0Count)
# 위 조건이 모두 아닐 시
else:
    # 누를수 있는 숫자버튼이 없는경우 +,-로만 움직임
    if len(usableNum) == 0:
        print(abs(int(n)-100))
    # 100에서 +,- 로 만들수 있는 경우
    # 중복순열(product)를 이용하여 완전탐색 하는 경우
    # 위 두 경우들 중 가장 최적화된 방법 출력
    else:
        compCount = abs(int(n)-100)
        for i in range(1, len(n)+2):
            prodNumList = list(itertools.product((usableNum),repeat=i))
            for j in range(len(prodNumList)):
                prodNum = "".join(prodNumList[j])
                subNum = abs(int(prodNum)-int(n))
                if subNum < resultSub:
                    resultNum = int(prodNum)
                    resultSub = subNum
        count = len(str(resultNum)) + resultSub
        if compCount < count:
            print(compCount)
        else:
            print(count)
        
et = time.time()
print("time : {}".format(et-st))