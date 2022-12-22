# 나는야 포켓몬 마스터 이다솜

# 해시테이블에 관한 문제임
# python은 dict로 구현할 수 있음
# 단, key와 value의 값을 하나의 dict로 저장하고 value로 key를 찾을려고
# 시도하면 list를 쓴것과 차이가 없으므로 시간초과가 됨.
# 따라서, dict를 두개 만들어서 각자 O(1)의 시간복잡도로 구현함.
# 중복 문제는 문제에서 도감이라고 하였으므로 문제 없음

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
bookOfName = {}
bookOfNum = {}
for i in range(1,n+1):
    name = sys.stdin.readline().rstrip()
    bookOfName[str(i)] = name
    bookOfNum[name] = i
for _ in range(m):
    quiz = sys.stdin.readline().rstrip()
    
    if quiz in bookOfName.keys():
        answer = bookOfName[quiz]
    else:
        answer = bookOfNum[quiz]
    print(answer)
        
