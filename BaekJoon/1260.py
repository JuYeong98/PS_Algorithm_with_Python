import sys
input = sys.stdin.readline
from collections import deque


def dfs(graph, v):
    visited = []
    stack = [v]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += reversed(graph[n])
    return visited

def bfs(graph, v):
    visited = []
    queue = deque([v])
    
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n]
    return visited

n, m, v = map(int, input().split())
n, m , v = map(int, input().split())
n, m ,v = map(int , input().split())

graph = {i:[] for i in range(1,n+1)}
for i in range(1, m+1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for key in graph:
    graph[key].sort()

print(' '.join(list(map(str,dfs(graph, v)))))
print(' '.join(list(map(str,bfs(graph, v)))))
