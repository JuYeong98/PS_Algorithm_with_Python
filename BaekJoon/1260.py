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


n, m, v = map(int, input().split())
n,m,v = map(int, input().split())

graph = {i:[] for i in range(1,n+1)}
for i in range(1, m+1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for key in graph:
    graph[key].sort()

print(' '.join(list(map(str,dfs(graph, v)))))
print(' '.join(list(map(str,bfs(graph, v)))))


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

from collections import deque
 
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visitied[i]:
                queue.append(i)
                visitied[i] = True

def bfs(graph , start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v= queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                    