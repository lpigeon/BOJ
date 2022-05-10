# DSLR

import sys
from collections import deque

def bfs(graph, v, w, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


t = int(sys.stdin.readline().rstrip())
visited = [False]*10000

for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip())
    a = list(str(a))
    bfs(graph, a, b, visited)
    
if x == "D":
    for i in a:
        
elif x == "D":
elif x == "D":
else:
