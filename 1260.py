# DFS와 BFS
import time
st = time.time()

#a, b, c = map(int, input().split())
#a, b = map(int, sys.stdin.readline().rstrip().split())

from collections import Counter, deque
import sys

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    # 현재 노드를 방문 처리
    visited[v] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [[]]
sub_graph = []
line = []
n, m, v= map(int, sys.stdin.readline().rstrip().split())
visited = [False]*(n+1)

for _ in range(m):
    line.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(1,n+1):
    for j in line:
        if i in j:
            sub_graph.append(sum(j)-i)
        sub_graph.sort()
    graph.append(sub_graph)
    sub_graph = []

dfs(graph,v,visited)
print("")
visited = [False]*(n+1)
bfs(graph,v,visited)
print("")


et = time.time()
print("time : {:.4f}".format(et-st))